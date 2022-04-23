import pandas as pd
import numpy as np
import math

df=pd.read_csv('M.csv', header=None)
#print(df)

q_0=pd.Series([1,0,0,0,0,0,0,0,0,0])
#print(q_0)
t=2048
t_0=100

def matrixPower(t, df, q_0):
    M_t=np.linalg.matrix_power(df.values, t)
    q=np.matmul(M_t, q_0.values)
    return q.tolist()


def statePropagation(t, df, q_0):
    q=q_0.values
    M=df.values
    for i in range(t):
        q=np.matmul(M, q)
    return q.tolist()

def randomWalk(t, df, q_0, t_0):
    state=[0,0,0,0,0,0,0,0,0,0]
    q=q_0.values
    M=df.values
    for j in range(t_0):
        q=np.matmul(M,q)
        k=np.argmax(q)
        state_temp=[0]*len(state)
        state_temp[k]=1
        q=state_temp
    q=(pd.Series([0,0,0,0,0,0,0,0,0,1]).values)
    for i in range(t):
        q=np.matmul(M, q)
        #print(q)
        sum_dist=np.cumsum(q)
        rand=np.random.rand()
        for i in range(len(sum_dist)):
            if sum_dist[i]>rand:
                k=i
                break
        state[k]+=1
    print(state)
    sumState=sum(state)
    return [float(i)/sumState for i in state]

def eigenAnalysis(t, df, q_0):
    M=df.values
    temp, temp_1=np.linalg.eig(M)
    result=[0]*10
    for i in  range(len(temp_1)):
        result[i]=temp_1[i][0]
    sumState=sum(result)
    print([float(i)/sumState for i in result])


#print('matrix power: ',matrixPower(t, df, q_0), '\\\\')
#print('state propagation: ',statePropagation(t, df, q_0), '\\\\')
print('random walk: ',randomWalk(t, df, q_0, t_0), '\\\\')
#print(eigenAnalysis(t, df, q_0))
