#!/usr/bin/env python3

# While his code does solve the problem,
# I feel like the solution is sloppy.
# It goes through the loops in a redundant way.
#
# I tried to optimize it a little, but I couldn't
# figure it out. Right now it finds the solution 
# then goes through all the different orders of the
# words.
#
# Maybe I was too tired when I wrote it, but 
# something minor is wrong with the recursion.
#
# I found the solution by using ./wordMatch.py | grep '15\['

def main():
    i=0
    j=0
#    dictPath = "/usr/share/dict/cracklib-small"
    dictPath = "/usr/share/dict/words"
    dictFull=loadDictionary(dictPath)
    
    # This set of words is sorted to test options for boat and
    # then find the most obvious matches.
    wordsToMatch=('boat','berry','butter','pass','plane','flower',
            'bow','fish','skate','pool','horse','fall',
            'rail','car','way','side',
            'board','back','sub','road','walk','water',
            'star','rain','fly','black','port','air','sun','up')
    """wordsToMatch=('flower','berry','bow','butter',
            'pass','plane','star','way','car','horse',
            'up','rail','boat','pool','back',
            'side','fish','fall','water','skate',
            'board','walk','road','sub','sun','black',
            'port','rain','fly','air')"""
    print("Words to match: " + str(len(wordsToMatch)) + "\n" +
            str(wordsToMatch))
    dictTrim=trimDict(dictFull,wordsToMatch)
    tempWords=findMatches(dictTrim,list(wordsToMatch))
    j = len(tempWords)
    print(str(j)  + " words in list\n" + str(tempWords))

def findMatches(dictionary, wordList, curMatches = []):
    tempList = wordList.copy()
    newTempL = []
    allFound = False
    recursiveMatches = []
    i = 0
    j = 0
    k = ""
    while not allFound and i < len(tempList):
        j = i + 1
        for x in tempList:
            if j > len(tempList) - 1: # catch out-of-range error
                break
            k = ""
            tempWord1 = tempList[i] + tempList[j]
            tempWord2 = tempList[j] + tempList[i]
            if checkDictionary(dictionary,tempWord1):
                k = tempWord1
            if checkDictionary(dictionary, tempWord2):
                k = tempWord2
            if k != "":
                curMatches.append(k)
                newTempL = tempList.copy()
                newTempL.remove(tempList[j])
                newTempL.remove(tempList[i])
                recursiveMatches = findMatches(dictionary,newTempL,curMatches)
                allFound = [] != recursiveMatches
                print(str(len(curMatches)) + str(curMatches) + " :: " + str(newTempL))
                #if len(newTempL) == 0: # I don't know why this doesn't work :(
                #    return recursiveMatches
                curMatches.remove(k)
            j += 1 
        i += 1
#        return [] # this return should be valid and prevent excess looping
# Although, it might need to be a break or something instead.
# Logic: if you can't find a match for a word, you should just give up on that
# path. Go back and try again.
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
