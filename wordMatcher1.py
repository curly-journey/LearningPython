#!/usr/bin/env python3
def main():
    i=0
    j=0
    dictPath = "/usr/share/dict/words"
    dictFull=loadDictionary(dictPath)
    wordsToMatch=('black','berry','sub','skate','air',
            'pass','water','way','flower','car','horse',
            'up','plane','rail','port','boat','pool','back',
            'side','fish','fall','sun','rain','butter','fly',
            'bow','star','board','walk','road')
    dictTrim=trimDict(dictFull,wordsToMatch)
    tempWords=findMatches(dictTrim,list(wordsToMatch))
    j = len(tempWords)
    print(str(j)  + " words in list\n" + str(tempWords))

def findMatches(dictionary, wordList, curMatches = []):
    tempList = wordList
    newTempL = []
    allFound = False
    recursiveMatches = []
    i = 0
    j = 0
    k = ""
    while not allFound and i < len(tempList):
        j = i + 1
#        if k != "":
#            print("i=" + str(i) + " j=" + str(j) + " len=" + str(len(tempList)))
        for x in tempList:
            if j >= len(tempList) - 1: # catch out-of-range error
                break
            k = ""
            tempWord1 = tempList[i] + tempList[j]
            tempWord2 = tempList[j] + tempList[i]
            if checkDictionary(dictionary,tempWord1):
                k = tempWord1
            if checkDictionary(dictionary, tempWord2):
                k = tempWord2
            if k != "":
                print(tempList)
                curMatches.append(k)
                newTempL = tempList.copy() #vitally important. lists = pointers
                newTempL.remove(str(tempList[j]))
                newTempL.remove(str(tempList[i]))
                if len(newTempL) + 2 != len(tempList):
                    print("HOW DOES REMOVE WORK?!  " + str(k))
                    print(newTempL)
                    print(tempList)
                    quit()
                recursiveMatches = findMatches(dictionary,newTempL,curMatches)
                allFound = [] != recursiveMatches
                if allFound == True:
                    print("Thinks it found them all!")
                print(curMatches)
                curMatches.remove(k)
            j += 1
        i += 1
    if len(tempList) == 0:
        return recursiveMatches
    else:
        return []



def trimDict(dictionary,wordList):
    newDict = []
    for x in dictionary:
        for y in wordList:
            if strContains(x,y):
                newDict.append(x.strip())
                break
    return newDict

def strContains(str1, str2):
    longStr = str1.lower()
    shortStr = str2.lower()
    longLen = len(longStr)
    shortLen = len(shortStr)
    if shortLen > longLen:
        longStr = shortStr
        shortStr = str1.lower()
        longLen = shortLen
        shortLen = len(shortStr)
    elif len(shortStr) == len(longStr):
        if shortStr == longStr:
            return True
        else:
            return False

    # At this point, we want to check the start and end of longStr
    # number of characters to check is shortLen.
    startStr = longStr[0:shortLen]
    endStr = longStr[longLen-shortLen : longLen]
    if startStr == shortStr or endStr == shortStr:
        return True
    else:
        return False

def checkDictionary(dictionary, word):
    match = False
    for x in dictionary:
        if x == word:
            match = True
            break
    return match

def loadDictionary(path):
    words=[]
    #count = 0
    f=open(path,"r")
    #f1 = f.readlines()
    for x in f:
    #    count += 1
        words.append(x)
    #print(str(count) + " words in the list")
    return words

main()
