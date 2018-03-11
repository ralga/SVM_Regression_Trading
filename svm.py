# pip install numpy, scipy, scikit-learn
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
import LoadCSV
import preprocessing as pp
import sys

def getData(values) :
    for i in range(0,len(values)) :
        values[i] = np.delete(values[i],len(values[i])-1,0)
    values,nbdata = pp.getLinear(values)
    return values



def trainSVM(svm,train,expTrain):
    support = [[1,2,3,4]]
    support = np.array(support)
    for i in range(0,len(train)) :
        svm = svm.fit(train[i], expTrain[i])
        support = np.concatenate([support,svm.support_vectors_],axis=0)
    np.delete(support,0,0)
    return support

def evaluate(svm,check,expcheck) :
    score = 0
    print (len(check), len(expcheck))
    for i in range(0, len(check)) :
        score += svm.score(check[i], expcheck[i])
    return score

def predict(svm, array) :
    return svm.predict(array)

def showData(svm,check,expcheck):
    array = predict(svm,check[len(check)-1])
    dates = list(range(1, len(array)+1))
    print (len(array)+1, len(dates))
    plt.plot(dates, array, color='cornflowerblue', lw=2, label='Polynomial model')
    plt.plot(dates, expcheck[len(check)-1], color='darkorange', label='data')

if __name__ == "__main__":
    svr_rbf = SVR(kernel='rbf', C=1e3,gamma=0.1,epsilon=0.01 ,degree=15,cache_size=1000,verbose=True)
    svr_sig = SVR(kernel='sigmoid', C=0.5,epsilon=0.01 ,degree=15,cache_size=1000,verbose=True)
    svr_poly = SVR(kernel='poly', C=1e3,epsilon=0.01 ,degree=5,cache_size=1000,verbose=True)
    print (svr_sig)
    values = getData()
    train,expTrain,check,expcheck = pp.setSvmValues(values)
    
    #svr_poly.support_vectors_ = trainSVM(svr_poly,train,expTrain)
    #svr_rbf.support_vectors_ = trainSVM(svr_rbf,train,expTrain)
    svr_sig.support_vectors_ = trainSVM(svr_sig,train,expTrain)
    #vectors = trainSVM(svr_sig,train,expTrain)
    #print(vectors)
    #print(svr_sig.support_vectors_)
    sys.stdout.flush()
    #svr_sig.support_vectors_ = vectors
    #print(svr_sig.support_vectors_)
    sys.stdout.flush()
    '''svr_sig = svr_sig.fit(train[len(train)-1], expTrain[len(train)-1])
    print (svr_sig.support_vectors_, "stuff")'''
    
    #print (svr_sig.support_vectors_)
    #trainSVM(svr_rbf,train,expTrain)
    #trainSVM(svr_poly,train,expTrain)
    #trainSVM(svr_sig,train,expTrain)
    #print (evaluate(svr_sig,check,expcheck))
    #print (evaluate(svr_poly,check,expcheck))
    #print (evaluate(svr_rbf,check,expcheck))
    #showData(svr_poly,check,expcheck)
    showData(svr_sig,check,expcheck)
    #showData(svr_rbf,check,expcheck)

    
    '''
    for dataset in values :
        plt.plot(dataset)
    #plt.plot(train)
    
    #plt.plot(values)
    plt.show()'''

def support_vectors_regression(data,kernel="rbf") :
    if (kernel == "rbf")
        svm = SVR(kernel='rbf', C=1e3,gamma=0.1,epsilon=0.01 ,degree=15,cache_size=1000,verbose=True)
    elif (kernel == "poly") :
        svm = SVR(kernel='poly', C=1e3,gamma=0.1,epsilon=0.01 ,degree=15,cache_size=1000,verbose=True)
    elif (kernel == "sigmoid"):
        svm = SVR(kernel='sigmoid', C=1e3,gamma=0.1,epsilon=0.01 ,degree=15,cache_size=1000,verbose=True)
    else:
        sys.exit("Argument denied")
    values = getData(data)
    train,expTrain,check,expcheck = preprocess(values)
    svm.support_vectors_ = trainSVM(svm,train,expTrain)
    return svm
