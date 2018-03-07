#!/usr/bin/env python
importTime=None
readFileTime=None
scaleTime=None
trainTime=None
predictTime=None

import time
st=time.time()
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler  
from sklearn.linear_model import PassiveAggressiveRegressor
importTime=time.time()-st
print("Time to import: "+str(importTime))
st=time.time()
scale=True 
#with scaling on, this seems to give a good "minimum" model, meaning the real value is always more then the predicted value, however somtimes by 
#alot
		
X=[]
Y=[]
#   [temp,sky,dayPercent,Max Power]
f=open("SolarData(4-6).csv")
print(f.readline())
data=f.readlines()
readFileTime=time.time()-st
print("Time to Read File: "+str(readFileTime))
st=time.time()
for line in data:
	l=line.split(",")
	X.append([int(l[2]),int(l[3]),int(l[1]),30])
	Y.append(int(l[0]))
if scale:
	scaler = StandardScaler()  
	Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,Y,test_size=0.33,random_state=42)
	scaler.fit(Xtrain)  
	Xtrain = scaler.transform(Xtrain)  
	Xtest = scaler.transform(Xtest)
scaleTime=time.time()-st
print("Time to split and Scale Data: "+str(scaleTime))

#X = [[0, 0], [2, 2]]
#y = [0.5, 2.5]
#clf = MLPRegressor(hidden_layer_sizes=(1000,), random_state=1, max_iter=1, warm_start=True)
clf = PassiveAggressiveRegressor(random_state=1,warm_start=True,max_iter=100)
st=time.time()
ttList=[]
for i in range(len(Xtrain)):
	tt=time.time()
	clf = clf.partial_fit(Xtrain, Ytrain)
	print(i/len(Xtrain))
	ttList.append(time.time()-tt)
trainTime=time.time()-st
joblib.dump(clf,'currentModel.mod')
pred=[]
st=time.time()
for x in range(len(Xtest)):
	pred.append(clf.predict([Xtest[x]]))
score=metrics.mean_absolute_error(Ytest,clf.predict(Xtest))
predictTime=time.time()-st
print("Time to import: "+str(importTime))
print("Time to Read File: "+str(readFileTime))
print("Time to split and Scale Data: "+str(scaleTime))
print("Time to train: "+str(trainTime))
print("Time to predict: "+str(time.time()-st))
print("Mean ABS error: %f" % score)

fig, ax = plt.subplots()
ax.plot(pred)
ax.plot(Ytest)

plt.show()
