import math
import random
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster
import pandas as pd


def misraGries(char, label, counter):
    if(char in labels):
        #print('here0')
        idx=labels.index(char)
        counter[idx]=counter[idx]+1
    else:
        flag=True
        for i in range(len(label)):
            if(counter[i]<=0 and flag):
                #print('here1')
                label[i]=char
                counter[i]=1
                flag=False
        if(flag):
            #print('here2')
            for i in range(len(label)):
                counter[i]=counter[i]-1
    return label, counter
        

with open('S1.txt') as f:
    charString=f.read()
k=7
labels=[]
counter=[]
j=0
for i in range(len(charString)):
    if j<k-1:
        if(charString[i] in labels):
            idx=labels.index(charString[i])
            counter[idx]=counter[idx]+1
        else:
            labels.append(charString[i])
            counter.append(1)
            j=j+1
    elif j==k-1:
        print(labels)
        j=j+1
    else:
        #print(charString[i])
        labels,counter=misraGries(charString[i], labels, counter)
print(labels, counter)
print([(num+len(charString)/k)/len(charString)*100 for num in counter])
#print([(num-len(charString)/k)/len(charString)*100 for num in counter])
print(len(charString))

with open('S2.txt') as f:
    charString=f.read()
k=7
labels=[]
counter=[]
j=0
for i in range(len(charString)):
    if j<k-1:
        if(charString[i] in labels):
            idx=labels.index(charString[i])
            counter[idx]=counter[idx]+1
        else:
            labels.append(charString[i])
            counter.append(1)
            j=j+1
    elif j==k-1:
        print(labels)
        j=j+1
    else:
        #print(charString[i])
        labels,counter=misraGries(charString[i], labels, counter)
print(labels, counter)
print([(num+len(charString)/k)/len(charString)*100 for num in counter])
#print([(num-len(charString)/k)/len(charString)*100 for num in counter])
print(len(charString))