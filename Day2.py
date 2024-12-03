import fileinput

#       ----- Part 1: Red-Nosed Reports -----
def isConsistent(line):
    if all(line[i] < line[i+1] for i in range(0,len(line) -1)):
        return True

    if all(line[i] > line[i+1] for i in range(0,len(line) -1)):
        return True

    return False

def safeDifference(line):
    return all(0 < abs(line[i] - line[i+1]) <= 3 for i in range(len(line) -1))

        
safeCount = 0
levelList = []

for line in fileinput.input(["Day2_input.txt"]):
    levelList = list(map(int, line.split()))
    
    if not isConsistent(levelList):
        continue
    
    if not safeDifference(levelList):
        continue
    
    safeCount += 1

print(safeCount)
        
#       ----- Part 2: Problem Dampener -----

def isConsistentPD(line):
    consistent = True
    for i in range(0,len(line) -1)):
        if line[i] <= line[i+1]:
            consistent = False

    if all(line[i] > line[i+1] for i in range(0,len(line) -1)):
        return True

    return False

def safeDifferencePD(line):
    return all(0 < abs(line[i] - line[i+1]) <= 3 for i in range(len(line) -1))
        

isProblem = 0
for line in fileinput.input(["Day2_input.txt"]):
    levelList = list(map(int, line.split()))
    
    if not isConsistent(levelList):
        isProblem += 1
    
    if not safeDifference(levelList):
        isProblem += 1

    if isProblem > 1:
        continue
    
    if 0 < is isProblem:
        problemDampener(line)
    
    safeCount += 1
