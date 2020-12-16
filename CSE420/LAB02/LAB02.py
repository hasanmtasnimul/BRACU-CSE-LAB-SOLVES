'''
lab 02
Md. Tasnimul Hasan
Fall 2020
'''


finalOutput = []
def isEmail(inp):
    numSet = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    speCharSet= (".", "-", "_")
    if "@" not in inp:
        return False
    if "@" in inp:
        temp = inp.split("@")
        #first half
        if temp[0].startswith(numSet) or temp[0].startswith(speCharSet) or temp[0]=="":
            return False

        for i in range(len(temp[0])):
            if not temp[0][i].isalpha():
                try:
                    if not (temp[0][i-1].isalpha() and temp[0][i+1].isalpha()):
                        return False
                except IndexError:
                    return False
        #last half
        if temp[1].endswith(numSet) or temp[1].endswith(speCharSet) or temp[1]=="":
            return False

        for i in range(len(temp[1])):
            if not temp[1][i].isascii():
                try:
                    if not (temp[1][i-1].isascii() and temp[1][i+1].isascii()):
                        return False
                except IndexError:
                    return False

    return True

def isWeb(inp):
    #assuming "www." is a must
    if not inp.startswith("www."):
        return False
    if inp.startswith("www."):
        temp = inp.split(".")
        if (len(temp) < 3) or ("" in temp):
            return False
        for i in range(1, len(temp)):
            #for middle part after www.
            if i == 1:
                for j in temp[1]:
                    if not j.isalpha():
                        return False
            #for other parts
            else:
                for j in temp[i]:
                    if not j.isascii():
                        return False
    return True







n = int(input())
for i in range(1, n+1):
    text = input()
    if isEmail(text):
        finalOutput.append("Email, " + str(i))
        continue
    if isWeb(text):
        finalOutput.append("Web, " + str(i))

for i in finalOutput:
    print(i)


