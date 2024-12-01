import fileinput
import time

#        ---- Part 1 -----

list1 = []
list2 = []

for line in fileinput.input(["Day1_input.txt"]):
    num1, num2 = line.split()
    list1.append(int(num1))
    list2.append(int(num2))
#sort the lists
sorted1 = tuple(sorted(list1))
sorted2 = tuple(sorted(list2))
#Pair the lists
pairList = []
for i in range(0, len(sorted1)):
    pairList.append(tuple((sorted1[i], sorted2[i])))
#Find distance
distance = []
for line in pairList:
    distance.append(abs(line[0] - line[1]))
#Sum of list
print(sum(distance))

#        ---- Part 2 -----
uniqueNumbers = list(set(sorted2))
#Create a table for efficient searching. {uniqueNumber : quantity}
quantity = {}
for number in uniqueNumbers:
    count = sorted2.count(number)
    quantity[number] = count

#Create a list of similarity scores:
#firstListNumber * quantityOfSecondListNumber
similarityList = []
for number in sorted1:
    volume = quantity.get(number,0)
    outputList.append(number * volume)

print(sum(similarityList))
