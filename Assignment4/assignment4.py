import math
import random
import csv
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.cluster.hierarchy import centroid, linkage, dendrogram
import scipy.spatial
def distance(point1, point2):
    dist=0
    for i in range(len(point1)):
        dist=dist+(point2[i]-point1[i])**2
    dist=math.sqrt(dist)
    return dist

def getLabels(dataSet, centers):
    labels=[]
    for data in dataSet:
        temp_label=i
            #if(dist>cost1):
            #    cost1=dist
            #cost2=cost2+dist**2
        labels.append(temp_label)
    return labels

with open('C1.txt') as f:
    lines=f.readlines()

data=[]
X=[]
Y=[]
for line in lines:
    line.replace('\n', '')
    data_str=line.split()
    data_nums=list(map(float, data_str))    
    X.append(data_nums[0])
    Y.append(data_nums[1])
    data.append(data_nums)
#print(data)

y=scipy.spatial.distance.pdist(data)
Z=linkage(y,method='centroid')
print(Z)
fig=plt.figure()
dendrogram(Z)
    
Label=[3,3,4,4,4,4,4,4,4,4,0,0,0,0,2,2,1,0,0,3]
plt.scatter(X, Y, c=Label)
plt.show()




