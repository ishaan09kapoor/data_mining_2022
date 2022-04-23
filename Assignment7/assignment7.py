import numpy as np
from scipy import linalg as LA
from matplotlib import pyplot as plt
import math
A = np.loadtxt('A.csv', delimiter=',')
U, S, Vt = LA.svd(A, full_matrices=False)

k=4
Sk=S[:k]
S=np.diag(S)
Sk=np.diag(Sk)
#print(A.shape)
'''for k in range(1,21):
    #print('k=',k, '\\\\')
    Uk = U[:,:k]
    Sk = S[:k,:k]
    Vtk = Vt[:k,:]
    Ak = Uk @ Sk @ Vtk
    l2norm=LA.norm(A-Ak,2)
    if (l2norm<0.3*LA.norm(A,2)):
        print(k)
        break'''
'''Vt=Vt[:2]
V=np.transpose(Vt)
SVD=A @ V
x=[]
y=[]
for val in SVD:
    x.append(val[0])
    y.append(val[1])
plt.title('Data in 2 dimensions')
plt.scatter(x,y)
plt.show()'''
#A=A[:100]

def freq_dir(A,l):
    r = A.shape[0]
    c = A.shape[1]
    B = np.zeros([l*2, c])
    B[:l-1, :] = A[:l-1,:]
    zerorows = l + 1
    #print(B)
    for i in range(l-1,r):
        zeroes=np.where(~B.any(axis=1))[0]
        #print(zeroes)
        try:
            B[zeroes[0]]=A[i]
        except:
            continue
        zeroes=np.where(~B.any(axis=1))[0]
        if(not np.any(zeroes)):
            print('a')
            U, S, Vt = LA.svd(B, full_matrices=False)
            S_new = np.zeros([len(S)])
            for i in range(l-1):
                S_new[i]=math.sqrt(S[i]**2-S[l-1]**2)
            print(S_new.shape)
            S_new=np.diag(S_new)
            B=S_new @ Vt           
    return B
k=0
Uk = U[:,:k]
Sk = S[:k,:k]
Vtk = Vt[:k,:]
Ak=Uk@Sk@Vtk
error_threshold=LA.norm(A-Ak, 'fro')**2/20
print(error_threshold)
for i in range(1,3500):
    B=freq_dir(A, i)
    error=LA.norm(A.T @ A -B.T@B)
    if(error<error_threshold):
        print(i)
        print(error)
        break
