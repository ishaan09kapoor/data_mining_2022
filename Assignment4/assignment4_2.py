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
k=4
count=0
cost=[]
for a in range(0,100):
    model=cluster.KMeans(n_clusters=k, init='k-means++', max_iter=1)
    fitModel=model.fit(dataSet)
    centersInitial=fitModel.cluster_centers_
    centers=centersInitial[:]
    for i in range(0,20):
        centers=lloyd(centers, dataSet)
    for j in range(len(centers)):
        flag=1
        #print(centersInitial[j][0], centers[j][0])
        if(round(centers[j][0],3)==round(centersInitial[j][0],3) and round(centers[j][1],3)==round(centersInitial[j][1],3)):
            continue
        else:
            flag=2
            break
    if(flag==1):
        count=count+1
    cost.append(fitModel.inertia_/len(dataSet))

print(cost)
x=np.sort(cost)
y=np.arange(len(cost))/float(len(cost))
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('CDF')
plt. plot(x,y,marker='o')
plt.show()
print(count)



