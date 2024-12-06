import fileinput

#       ----- Part 1: Red-Nosed Reports -----
def isConsistent(line):
    if all(line[i] < line[i+1] for i in range(0,len(line) -1)):
        return True

    if all(line[i] > line[i+1] for i in range(0,len(line) -1)):
        return True

    return False

# Issue, abs() doesn't work properly for when applied with problem dampener.
# 
# def safeDifference(line):
#     return all(0 < abs(line[i] - line[i+1]) <= 3 for i in range(len(line)-1))

def reeseSafeDifference(levels):
    diffs = [x - y for x, y in zip(levels, levels[1:])]
    return all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)

def problemDampener(line):
        possibleArrays = []
        for i in range(len(line)):
             possibleArrays.append(line[:i]+line[i+1:])
        
        for array in possibleArrays:
             if isConsistent(array) and reeseSafeDifference(array):
                  return True
        return False

safeCount = 0
levelList = []
pdCheck = False

for line in fileinput.input(["Day2_input.txt"]):
    levelList = list(map(int, line.split()))
    
    if not reeseSafeDifference(levelList):
        if problemDampener(levelList):
            safeCount += 1
    else:
         safeCount += 1

print(safeCount)