import math
import random
import csv
import numpy as np
import matplotlib.pyplot as plt

def sos(vector):
    sum=0
    for ele in vector:
        sum=sum+ele*ele
    return sum
t=180
d=3
tau=0.7
vector=[]
for i in range(t):
    temp=[]
    for j in range(d):
        u1=random.uniform(0,1)
        u2=random.uniform(0,1)
        temp.append(math.sqrt(-2*np.log(u1))*math.cos(2*math.pi*u2))
    sumOfSquare=math.sqrt(sos(temp))
    vector.append([number/sumOfSquare for number in temp])

resultVal=[]
usefulVal=[]


for i in range(len(vector)):
    for j in range(i+1, len(vector)):
        dotProd=sum(k[0] *k[1] for k in zip(vector[i], vector[j]))
        sim=dotProd
        sim=1-math.acos(dotProd)/math.pi
        resultVal.append(sim)
        if(sim>tau):
            usefulVal.append(sim)
print(len(usefulVal))
x=np.sort(resultVal)
y=np.arange(len(resultVal))/float(len(resultVal))
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('CDF')
plt. plot(x,y,marker='o')
plt.show()