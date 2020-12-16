'''
lab 01
Md. Tasnimul Hasan
Fall 2020
'''

inputFile = open("input.txt", "r")

keywords = ("int", "float", "if", "else")
mathOps = ("+", "-", "*", "/", "=")
logicalOps = ("<", ">")
others = (",", ";", "(", ")", "{", "}")

keywordsSet = set()
mathOpsSet = set()
logicalOpsSet = set()
othersSet = set()
identifiersSet = set()
numValsSet = list()

def whatType(x):
    x = x.strip()
    if x.endswith(others):
        othersSet.add(x[-1])
        x = x[0:-1]

    if x in keywords:
        keywordsSet.add(x)
    elif x in mathOps:
        mathOpsSet.add(x)
    elif x in logicalOps:
        logicalOpsSet.add(x)
    elif x in others:
        othersSet.add(x)
    else:
        try:
            x = int(x)
            if x not in numValsSet:
                numValsSet.append(str(x))
        except ValueError:
            if "." in x:
                if x not in numValsSet:
                    numValsSet.append(str(x))
            else:
                identifiersSet.add(x)

for line in inputFile:
    lineStr = line.strip()
    lineStr = lineStr.split()
    for word in lineStr:
        whatType(word)

#removing empty string from the identifiers
identifiersSet.remove("")

print("keywords: ", end="")
print(*keywordsSet ,sep=", ")

print("Identifiers: ", end="")
print(*identifiersSet ,sep=", ")

print("Math Operators: ", end="")
print(*mathOpsSet ,sep=", ")

print("Logical Operators: ", end="")
print(*logicalOpsSet ,sep=", ")

print("Numerical Values: ", end="")
print(*numValsSet, sep=", ")

print("Others: ", end="")
print(*othersSet ,sep=" ")
