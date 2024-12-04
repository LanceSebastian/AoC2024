import fileinput

#   ----- Day 4: Ceres Search -----

# Part 2: MAS in X
def findCrossMAS(array, x,y):
    xMax = len(array[y])
    yMax = len(array)
    
    if y <= 1 or y > yMax - 2:
        return 0
    if x <= 1 or x > xMax - 2:
        return 0
    
    content = []
    expression1 = ""
    expression2 = ""

    

    content = [array[y-1][x-1] + '.' + array[y-1][x+1],
               '.' + array[y][x] + '.',
               array[y+1][x-1] + '.' + array[y+1][x+1] 
               ]

    for string in content:
        if 'X' in string:
            return 0

    #print(content)

    #print(f"{x},{y}")
    
    expression1 = content[0][0]+content[1][1]+content[2][2]
    expression2 = content[2][0]+content[1][1]+content[0][2]

    #print(f"({expression1})({expression2})")

    if expression1 == "MAM" or expression1 == "SAS":
        #print(f"({expression1})({expression2})")
        return 0
    if expression2 == "SAS" or expression2 == "MAM":
        #print(f"({expression1})({expression2})")
        return 0
    
    return 1

# Search surrounding directions for XMAS
def findXMAS(array, x, y):
    contents = []
    expression = ""

    xMax = len(array[0])
    yMax = len(array)
    
    right = x < xMax - 3
    left = x >= 3
    up = y >= 3
    down = y < yMax - 3

    if right:
        expression = array[y][x] + array[y][x+1] + array[y][x+2] + array[y][x+3]
        contents.append(expression)
    if left:
        expression = array[y][x] + array[y][x-1] + array[y][x-2] + array[y][x-3]
        contents.append(expression)
    if up:
        expression = array[y][x] + array[y-1][x] + array[y-2][x] + array[y-3][x]
        contents.append(expression)
    if down:
        expression = array[y][x] + array[y+1][x] + array[y+2][x] + array[y+3][x]
        contents.append(expression)
    if down and right:
        expression = array[y][x] + array[y+1][x+1] + array[y+2][x+2] + array[y+3][x+3]
        contents.append(expression)
    if down and left:
        expression = array[y][x] + array[y+1][x-1] + array[y+2][x-2] + array[y+3][x-3]
        contents.append(expression)
    if up and right:
        expression = array[y][x] + array[y-1][x+1] + array[y-2][x+2] + array[y-3][x+3]
        contents.append(expression)
    if up and left:
        expression = array[y][x] + array[y-1][x-1] + array[y-2][x-2] + array[y-3][x-3]
        contents.append(expression)

    return sum(line.count("XMAS") for line in contents)

count = 0
wordSearch = []

for line in fileinput.input(["Day4_input.txt"]):
    wordSearch.append(line.strip())

for y, line in enumerate(wordSearch):
    for x, char in enumerate(line):
        if char == 'A':
            count += findCrossMAS(wordSearch, x, y)
print(count)