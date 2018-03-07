#!/usr/bin/env python
from sklearn.model_selection import train_test_split
from sklearn import tree, metrics
import matplotlib.pyplot as plt
import numpy as np
from sklearn.externals import joblib

		
X=[]
Y=[]
#   [temp,sky,dayPercent,Max Power]
f=open("SolarData(4-6).csv")
print(f.readline())
data=f.readlines()
for line in data:
	l=line.split(",")
	X.append([l[2],l[3],l[1],30])
	Y.append(float(int(l[0])))

Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,Y,test_size=0.33,random_state=42)



#X = [[0, 0], [2, 2]]
#y = [0.5, 2.5]
clf = tree.DecisionTreeRegressor()
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
