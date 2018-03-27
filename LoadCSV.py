import csv

def read(path) :
    values = []
    with open(path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            aux = []
            aux.append(float(row[1]))
            aux.append(float(row[2]))
            aux.append(float(row[3]))
            aux.append(float(row[4]))
            aux.append(float(row[5]))
            values.append(aux)
    return values