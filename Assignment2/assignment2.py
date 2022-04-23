import glob
import os
import random
import time

def splitstring2Chars(str):
    return [char for char in word]


def unique(listy):
    uniqueList=[]
    for ele in listy:
        if ele not in uniqueList:
            uniqueList.append(ele)
    return uniqueList

def createHFunction(n,k):
    h=[]
    masterList=list(range(1,n+1))
    #print(temp)
    for i in range(k):
        temp=masterList
        random.shuffle(temp)
        h.append(temp[:])
    return h

def getFirstOne(h, vectorList):
    for i in range(len(h)):
        #print(h[i])
        if(vectorList[h[i]-1]==1):
            #print('h',h[i], 'V', vectorList[h[i]])
            return i+1



def minHashing(vectorList, k):
    tempVector=[]
    for i in range(len(vectorList)):
        tempVector.append([100000]*k)
    h=createHFunction(len(vectorList[0]), k)
    for i in range(len(vectorList)):
        for j in range(k):
            #print(i, j, h[j][:5], vectorList[i][:10])
            #print('j, ',j)
            #print('hj, ', len(h[j]))
            hji=getFirstOne(h[j], vectorList[i])
            #print('ij',tempVector[i][j])
            if(hji<tempVector[i][j]):
                #print('hji',hji)
                tempVector[i][j]=hji
                #print(tempVector)
    i=0
    j=1
    count=0
    for n in range(k):
        if(tempVector[i][n]==tempVector[j][n]):
            count=count+1
    return count/k
    '''for i in range(len(vectorList)):
        for j in range(i+1, len(vectorList)):
            count=0
            for n in range(k):
                if(tempVector[i][n]==tempVector[j][n]):
                    count=count+1
            print(i+1, j+1, count/k)'''           

twoGramMaster=[]
threeGramMaster=[]
charGramMaster=[]
for filepath in glob.glob('/home/u1301931/DM/assignment2/documents/*.txt'):
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        text=f.read()
    words=text.split()
    twoGramList=[]
    threeGramList=[]
    charGramList=[]
    #print(words)
    for i in range(0, len(words)-1):#
        if ([words[i], words[i+1]] not in twoGramList):
            twoGramList.append([words[i], words[i+1]])
        if  (i<len(words)-2):
            if ([words[i], words[i+1], words[i+2]] not in threeGramList):
                threeGramList.append([words[i], words[i+1], words[i+2]])
    chars=list(text)
    chars_f=[]
    for char in chars:
        if char != '\n':
            chars_f.append(char)
    chars=chars_f
    #print(chars)
    for i in range(0, len(chars)-2):
            if ([chars[i], chars[i+1], chars[i+2]] not in charGramList):
                charGramList.append([chars[i], chars[i+1], chars[i+2]])
    #print(2, len(twoGramList))
    #print(3, len(threeGramList))
    print('char', len(charGramList))
    twoGramMaster.append(twoGramList)
    threeGramMaster.append(threeGramList)
    charGramMaster.append(charGramList)
'''
print('twoGram')
for i in range(0, len(twoGramMaster)):
    for j in range(i, len(twoGramMaster)):
        if(i!=j):
            #twoGramListMain=[twoGramMaster[i], twoGramMaster[i]]
            #unionSet=set().union(*twoGramListMain)
            #print(unionSet)
            intersection=len([twoGram for twoGram in twoGramMaster[i] if twoGram in twoGramMaster[j]])
            union=len(unique(twoGramMaster[i]+twoGramMaster[j]))
            print(i+1,j+1,1.0*intersection/union)

print('threeGram')
for i in range(0, len(threeGramMaster)):
    for j in range(i, len(threeGramMaster)):
        if(i!=j):
            #twoGramListMain=[twoGramMaster[i], twoGramMaster[i]]
            #unionSet=set().union(*twoGramListMain)
            #print(unionSet)
            intersection=len([threeGram for threeGram in threeGramMaster[i] if threeGram in threeGramMaster[j]])
            union=len(unique(threeGramMaster[i]+threeGramMaster[j]))
            print(i+1,j+1,1.0*intersection/union)                  

print('charGramM')
for i in range(0, len(charGramMaster)):
    for j in range(i, len(charGramMaster)):
        if(i!=j):
            #twoGramListMain=[twoGramMaster[i], twoGramMaster[i]]
            #unionSet=set().union(*twoGramListMain)
            #print(unionSet)
            intersection=len([charGram for charGram in charGramMaster[i] if charGram in charGramMaster[j]])
            union=len(unique(charGramMaster[i]+charGramMaster[j]))
            print(i+1,j+1,1.0*intersection/union)  
'''          


allCharGrams=unique(charGramMaster[0]+charGramMaster[1]+charGramMaster[2]+charGramMaster[3])
#print(allCharGrams)
charGramVector=[]
for charGram in charGramMaster:
    wordVector=[]
    for charGramI in range(0,len(allCharGrams)):
        if(allCharGrams[charGramI] in charGram):
            wordVector.append(1)
        else:
            wordVector.append(0)
    charGramVector.append(wordVector)

for k in range(100, 5002, 100):
    #print(k)
    start=time.time()
    val=minHashing(charGramVector, k)
    end=time.time()
    print(str(val)+','+str(end-start)+','+str(k))