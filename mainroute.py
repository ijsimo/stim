import csv

class Runner:
    def __init__(self, fname, sname, s):
        self.fname = fname
        self.sname = sname
        self.distance = float(s)

def readData(filename):
    members = []
    f = open(filename, 'r')
    with f:
        reader = csv.reader(f)
        for row in reader:
            members.append(Runner(row[0], row[1], float(row[2])))
    f.close()
    return members

def FindMax(m):
    ##initialise max with first value
    maxVal = None
    ##loop through each entry in members
    for d in m:
        if maxVal == None:
            maxVal = d.distance
        elif d.distance > maxVal:
            maxVal = d.distance
    return maxVal

def Awards(m, l):
    ##m is the list of performances, l is the performance limit
    a = []
    for p in m:
        if p.distance > l:
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
    for a in awards:
        print(a.fname + " " + a.sname + " " + str(a.distance))

Main()
                
