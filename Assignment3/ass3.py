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
vector=[]
with open('R.csv') as csvfile:
    spamreader=csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        member=[]
        for ele in row:
            member.append(float(ele))
        vector.append(member[:])
vector=vector[0:450]
resultVal=[]
usefulVal=[]
for i in range(len(vector)):
    for j in range(i+1, len(vector)):
        dotProd=0
        for k in range(0, len(vector[0])):
            dotProd=dotProd+vector[i][k]*vector[j][k]
        dotProd=dotProd/math.sqrt(sos(vector[i])*sos(vector[j]))
        sim=1-math.acos(dotProd)/math.pi
        resultVal.append(sim)
        if(sim>0.70000):
            usefulVal.append([i,j,sim])
print(len(usefulVal))
x=np.sort(resultVal)
y=np.arange(len(resultVal))/float(len(resultVal))
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('CDF')
plt. plot(x,y,marker='o')
plt.show()
#print(usefulVal)
