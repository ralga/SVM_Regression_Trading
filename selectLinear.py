
def getLinear(values) :
    i = 0
    final = []
    j = values[i]
    aux = []
    comp = 0
    while i < (len(values)-1) :
        if(checkDist(j,values[i+1])) :
            aux.append(values[i+1])
        else:
            if(len(aux)>30) :
                final.append(aux)
            comp +=len(aux)
            aux = []
            j = values[i]
        i+=1
    if(len(aux)>30) :
        final.append(aux)
    else:
        comp +=len(aux)
    return (final,comp)

def checkDist(ref, todo) :
    return (not (todo[0]>(ref[0] + (ref[0]*2)/100) or todo[0] <(ref[0] - (ref[0]*2)/100))) and (not (todo[3]>(ref[3] + (ref[3]*2)/100) or todo[3] <(ref[3] - (ref[3]*2)/100)))