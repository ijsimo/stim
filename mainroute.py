import csv

def readData(filename):
    members = []
    f = open(filename, 'r')

    with f:
        reader = csv.reader(f)

        for row in reader:
            members.append((row[0], row[1], row[2]))
    f.close()
    return members

def FindMax(m):
    ##initialise max with first value
    maxVal = float(m[0][2])
    ##loop through each entry in 
    for d in m:
        if float(d[2]) > maxVal:
            maxVal = float(d[2])
    return maxVal

def Awards(m, l):
    ##m is the list of performances, l is the performance limit
    a = []
    for p in m:
        if float(p[2]) > l:
            a.append(p)
    return a

def Main():
    ##load data from file as named
    members = readData('members.csv')
    ##find the largest number in column 2 of returned array
    maxVal = FindMax(members)
    print('Max Value: ' + str(maxVal))
    ##find everyone with a score at least 70% of the maximum
    awards = Awards(members, 0.7 * maxVal)
    print(awards)

Main()
                
