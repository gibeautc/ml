#!/usr/bin/env python
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler  

scale=True 
#with scaling on, this seems to give a good "minimum" model, meaning the real value is always more then the predicted value, however somtimes by 
#alot
		
X=[]
Y=[]
#   [temp,sky,dayPercent,Max Power]
f=open("SolarData(4-6).csv")
print(f.readline())
data=f.readlines()
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


#X = [[0, 0], [2, 2]]
#y = [0.5, 2.5]
clf = MLPRegressor(hidden_layer_sizes=(1000,), random_state=1, max_iter=100, warm_start=True)
for i in range(len(Xtrain)):
	clf = clf.fit(Xtrain, Ytrain)
joblib.dump(clf,'currentModel.mod')
#print(clf.predict([[45,50,80,5]]))
pred=[]
for x in range(len(Xtest)):
	pred.append(clf.predict([Xtest[x]]))
score=metrics.mean_absolute_error(Ytest,clf.predict(Xtest))
print("Mean ABS error: %f" % score)

fig, ax = plt.subplots()
ax.plot(pred)
ax.plot(Ytest)

plt.show()
