import random
import numpy as np
import matplotlib.pyplot as plt
import time

def solve(nums, x, y) :
   temp_range = y - x
   for i in range(0, len(nums)):
      if abs(nums[i]) >= x and abs(nums[i]) <= y:
         z = abs(nums[i]) - x
         if (nums[z] > 0) :
            nums[z] = nums[z] * -1
   cnt = 0
   for i in range(0, temp_range + 1):
      if i >= len(nums):
         break
      if nums[i] > 0:
         return False
      else:
         cnt += 1
   if cnt != temp_range + 1:
      return False
   return True

countList=[]

m=500
n=250
start = time.time()
for i in range(0, m):
    numList=[]
    flag=True
    count=0
    while(flag):
        num=random.randrange(1,n+1)
        numList.append(num)
        if(count<n):
            count=count+1
        else:
            check=solve(numList, 0, n)
            if(check):
                print(i)
                flag=False
end=time.time()
#print('end')
elapsedTime=end-start
print(elapsedTime)


     
