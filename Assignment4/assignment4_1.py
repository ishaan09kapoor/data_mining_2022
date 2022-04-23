import math
import random
import csv
import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn import cluster
import pandas as pd

def distance(point1, point2):
    dist=0
    for i in range(len(point1)):
        dist=dist+(point2[i]-point1[i])**2
    dist=math.sqrt(dist)
    return dist

def getLabels(dataSet, centers):
    labels=[]
    for data in dataSet:
        min_dist=10000000000
        for i in range(len(centers)):
            dist=distance(data,centers[i])
            if dist<min_dist:
                min_dist=dist
                temp_label=i
            #if(dist>cost1):
            #    cost1=dist
            #cost2=cost2+dist**2
        labels.append(temp_label)
    return labels

def lloyd(centers, dataset):
    labelsI=getLabels(dataset, centers)
    groupeddatadf=pd.DataFrame({'X':X, 'Y':Y, 'Labels': labelsI}).groupby(['Labels'])
    newCenters=groupeddatadf.mean()
    #print(newCenters)
    return(newCenters.values.tolist())



with open('C2.txt') as f:
    lines=f.readlines()

dataSet=[]
X=[]
Y=[]
for line in lines:
    line.replace('\n', '')
    data_str=line.split()
    data_nums=list(map(float, data_str))    
    X.append(data_nums[0])
    Y.append(data_nums[1])
    dataSet.append(data_nums)
k=3
costs2=[]
count=0
#print([dataSet[0],dataSet[1],dataSet[2],dataSet[3]])
for p in range(20):
    #print(p)
    initCenter=dataSet[0]
    rand=int(random.uniform(0,len(dataSet)))
    centers=[dataSet[0]]
    labels=getLabels(dataSet, centers)

    for i in range(k):
        #prinflag=True[]
        prob=[]
        for t in range(len(dataSet)):
            #print(i,t,centers[labels[t]], dataSet[t])
            dist=distance(centers[labels[t]], dataSet[t])
            '''if(dist>max_dist):
                max_dist=dist
                newCenter=dataSet[t]'''
            prob.append(dist)
        '''if(dist>0):
            centers.append(newCenter[:])'''
        probF=[num/sum(prob)for num in prob]
        probCDF=np.cumsum(probF)
        rand=random.uniform(0,1)
        for l in range(len(probCDF)):
            if(rand<=probCDF[l]):
                final_i=l
                break
            else:
                final_i=0
        centers.append(dataSet[final_i])
        labels=getLabels(dataSet, centers)
        #print(labels)
        print(centers)
    X_cent=[]
    Y_cent=[]
    #centers=[dataSet[0],dataSet[1],dataSet[2],dataSet[3]]
    cent_inital=centers
    labelsI=getLabels(dataSet, centers)
    '''for i in range(0,20):
        centers=lloyd(centers, dataSet)'''
    
    for center in centers:
        X_cent.append(center[0])
        Y_cent.append(center[1])
    
    cost1=0
    cost2=0
    labels=getLabels(dataSet, centers)
    flag=True
    for s in range(len(labels)):
        if(labels[s]==labelsI[s]):
            flag=True
        else:
            flag=False
            break
    if(flag):
        count=count+1
    for n in range(len(dataSet)):
        dist=distance(dataSet[n], centers[labels[n]])
        cost2=cost2+dist*dist
        if dist>cost1:
            cost1=dist    
    cost2=math.sqrt(cost2/len(dataSet))
    '''plt.scatter(X, Y, c=labels, marker='.')
    plt.scatter(X_cent, Y_cent, marker='^')
    plt.show()
    '''
    print(cost1,cost2)
    costs2.append(cost2)
print(count)
x=np.sort(costs2)
y=np.arange(len(costs2))/float(len(costs2))
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('CDF')
plt. plot(x,y,marker='o')
plt.show()
