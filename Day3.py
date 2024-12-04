import fileinput
import re

#       ----- Mull It Over -----

# Part 2 function. Dictates if parse_and_multiply is allowed.
def doOrDont(expression, do):
    doMatch = re.search(r"do\(\)",expression)
    dontMatch = re.search(r"don\'t\(\)",expression)

    if doMatch:
        return True
    elif dontMatch:
        return False
    else:
        return do

# finds expressions "mul(X,Y)" where X and Y are 1-3 digit integers,
# then multiplies them.
def parseAndMultiply(expression, do):
    match = re.search(r"mul\((\d{1,3}),(\d{1,3})\)", expression)

    if match and do:
        X = int(match.group(1))
        Y = int(match.group(2))

        result = X * Y
        return result
    else:
        raise ValueError("Invalid format")

# reads each character into an expression and sends an
# expression every ')' character.
do = True
mulStore = []

for line in fileinput.input(["Day3_input.txt"]):
    expression = ""
    for char in line:
        expression += char
        if char == ')':
            try:
                do = doOrDont(expression, do)
                result = parse_and_multiply(expression, do)
                mulStore.append(result)
            except ValueError:
                pass
            finally:
                expression = ""

print(sum(mulStore))
