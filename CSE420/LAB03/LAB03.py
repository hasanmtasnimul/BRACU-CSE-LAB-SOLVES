'''
lab 03
Md. Tasnimul Hasan
Fall 2020
'''

import re

regexPatternList = []
textList = []
patternTimes = int(input())

#pattern input
for i in range(patternTimes):
    regexPattern = input()
    regexPatternList.append(regexPattern)

#text input
textTimes = int(input())
for i in range(textTimes):
    text = input()
    textList.append(text)

#match checking
for i in textList:
    matched = False
    for j in range(len(regexPatternList)):
        if re.match(regexPatternList[j], i):
            matched = True
            print("YES, ", j+1)
    if not matched:
        print("NO, 0")

