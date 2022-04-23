import math
import random
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
import pandas as pd

X=pd.read_csv('X.csv', header=None).to_numpy()

Y=pd.read_csv('y.csv', header=None).to_numpy()
X_temp=X.tolist()
Y_temp=Y.tolist()
#Y_temp=[num[0] for num in Y_temp]
#print(Y_temp)
alphaList=[0.1,0.3,0.7,0.9,1.1,1.3,1.5]

X1 = X[:75, :]
Y1 = Y[:75]
X2 = X[25:, :]
Y2 = Y[25:]
X3 = np.vstack((X[:50, :], X[75:, :]))
Y3 = np.concatenate((Y[:50], Y[75:]))
X4 = np.vstack((X[:25, :], X[50:, :]))
Y4 = np.concatenate((Y[:25], Y[50:]))
X_final=[X1,X2,X3,X4]
Y_final=[Y1,Y2,Y3,Y4]
#print(y)
'''
model=LinearRegression(fit_intercept=False)
fitModel=model.fit(X,Y)
#print('coeffecients:',fitModel.coef_, '\\\\')
print('Least Square coeffecients:',[round(num,3) for num in fitModel.coef_[0]], '\\\\')
y_pred=fitModel.predict(X)
#y_pred=pd.Series(y_pred)
#y=Y_final[i].values.tolist()
#print(y)
#print(y_pred)
#print(np.transpose(y_pred))
error=np.linalg.norm(Y-y_pred, 2)
print('error=', round(error,3),'\\\\')
for alpha in alphaList:
    y=pd.read_csv('y.csv', header=None)
    model=Ridge(alpha=alpha, fit_intercept=False)
    fitModel=model.fit(X,y)
    print('s=',alpha,' coeffecients:',[round(num,3) for num in fitModel.coef_[0]], '\\\\')
    y_pred=fitModel.predict(X)
    #y_pred=pd.Series(y_pred)
    y=y.values.tolist()
    #print(y)
    #print(y_pred)
    #print(np.transpose(y_pred))
    error=np.linalg.norm(y-y_pred, 2)
    print('error=', round(error,3),'\\\\')
'''
error=0
for i in range(len(X_final)):
    model=LinearRegression(fit_intercept=False)
    fitModel=model.fit(X_final[i],Y_final[i])
    #Y_test=[num[0] for num in Y_test]
    y_pred=fitModel.predict(X_final[i])
    #print(len(y_pred))
    #y_pred=pd.Series(y_pred)
    #y=Y_final[i].values.tolist()
    #print(y)
    #print(y_pred)
    #print(np.transpose(y_pred))
    error=np.linalg.norm(Y_final[i]-y_pred, 2)
    print('Error for linear regression  for dataset', str(i+1),'=', round(error,3),'\\\\')
#print('Avg error for linear regression =', round(error/4,2),'\\\\')
for alpha in alphaList:
    for i in range(len(X_final)):    
        model=Ridge(alpha=alpha)
        fitModel=model.fit(X_final[i],Y_final[i])
        #print('s=',alpha,' coeffecients:',[round(num,2) for num in fitModel.coef_[0]], '\\\\')
        y_pred=fitModel.predict(X_final[i])
        #y_pred=pd.Series(y_pred)
        #y=Y_final[i].values.tolist()
        #print(y)
        #print(y_pred)
        #print(np.transpose(y_pred))
        error=np.linalg.norm(y_pred-Y_final[i], 2)
        print('error for (s=',alpha,'dataset=',str(i+1),')=', round(error/4,3),'\\\\')



