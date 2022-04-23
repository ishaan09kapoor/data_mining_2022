import random
import numpy as np
import time

def solve(nums, n):
    numset=set(nums)
    if len(numset)==n:
        return True
    return False

timeList=[]
m=500
n=250
print(m,n)
start=time.time()
for i in range (0,m):
    print(i)
    numList=[]
    count=0
    flag=True
    while(flag):
        num=random.randrange(1,n+1)
        numList.append(num)
        if(count<n):
            count=count+1
        else:
            check=solve(numList, n)
            if(check):
                flag=False
end=time.time()
elapsedTime=end-start
print(elapsedTime)
timeList.append(elapsedTime)

print(timeList)