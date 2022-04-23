import math
import random
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster
import pandas as pd
import hashlib

_memomask = {}

hashFamily=[]



with open('S1.txt') as f:
    charString=f.read()
k=9
t=7
counter=np.zeros((t,k), dtype=int)
for i in range(t):
    hashFamily.append([random.randrange(0,67), random.randrange(0,67)])

for char in charString:
    for i in range(t):
        hashFun=hashFamily[i]
        counterNum=((hashFun[0]*ord(char)+hashFun[1])%67)%k
        counter[i][counterNum]=counter[i][counterNum]+1
print(counter)

toFind='a'
min=100000000
for i in range(t):
    hashFun=hashFamily[i]
    counterNum=((hashFun[0]*ord(toFind)+hashFun[1])%67)%k
    #print(counterNum)
    if(counter[i][counterNum]<min):
        min=counter[i][counterNum]
print(min)
toFind='b'
min=100000000
for i in range(t):
    hashFun=hashFamily[i]
    counterNum=((hashFun[0]*ord(toFind)+hashFun[1])%67)%k
    #print(counterNum)
    if(counter[i][counterNum]<min):
        min=counter[i][counterNum]
print(min)
toFind='c'
min=100000000
for i in range(t):
    hashFun=hashFamily[i]
    counterNum=((hashFun[0]*ord(toFind)+hashFun[1])%67)%k
    #print(counterNum)
    if(counter[i][counterNum]<min):
        min=counter[i][counterNum]
print(min)