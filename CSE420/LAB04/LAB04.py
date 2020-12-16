'''
lab 04
Md. Tasnimul Hasan
Fall 2020
'''

import re

inputFile = open("input.txt", "r")
methods = []

methodPattern = r"(public|private|protected|default)( static)? (Boolean|char|byte|short|int|long|float|double|String|void) \w+\((.*)?\)"
mainMethodPattern = r"public static void main(.*)"

for line in inputFile:
    if re.match(methodPattern, line) and not re.match(mainMethodPattern, line) :
        methods.append(re.findall("(Boolean|char|byte|short|int|long|float|double|String|void) (\w+)\((.+)?\)", line)[0])

print("Methods:")
for m in methods:
    print("{} ({}), return type: {}".format(m[1], m[2], m[0]))


