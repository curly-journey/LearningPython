#!/usr/bin/env python3
def main():
    i=0
    j=0
    dictPath = "/usr/share/dict/words"
    fullDict=loadDictionary(dictPath)
    wordsToMatch=('black','berry','sub','skate','air',
            'pass','water','way','flower','car','horse',
            'up','plane','rail','port','boat','pool','back',
            'side','fish','fall','sun','rain','butter','fly',
            'bow','star','board','walk','road')
    trimDict=trimDictionary(fullDict,wordsToMatch)
    tempWords=list(wordsToMatch)
    for x in tempWords:
        i += 1
    print(str(i) + " words in list\n" + str(tempWords))

def trimDict(dictionary,wordList):
    newDict = []
    for x in dictionary:
        for y in wordList:
            if strContains(x,y):
                newDict.append(x)
                break
    return newDict

def checkDictionary(word, dictionary):
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
