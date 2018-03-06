#!/usr/bin/env python


class dataPoint:
	def __init__(self):
		self.temp=0
		self.sky=0
		self.dayPercent=0
		self.maxPower=0
		self.current=0
		
		
X=[]
Y=[]
#   [temp,sky,dayPercent,Max Power]
X.append([50,0,0,5])
X.append([50,0,10,5])
X.append([50,0,20,5])
X.append([50,0,30,5])
X.append([50,0,40,5])
X.append([50,0,50,5])
X.append([50,0,60,5])
X.append([50,0,70,5])
X.append([50,0,80,5])
X.append([50,0,90,5])
X.append([50,0,100,5])

# output current
Y.append(20.0)
Y.append(50.0)
Y.append(70.0)
Y.append(90.0)
Y.append(100.0)
Y.append(200.0)
Y.append(100.0)
Y.append(70.0)
Y.append(50.0)
Y.append(40.0)
Y.append(10.0)


X.append([50,0,50,5])
X.append([50,10,50,5])
X.append([50,20,50,5])
X.append([50,30,50,5])
X.append([50,40,50,5])
X.append([50,50,50,5])
X.append([50,60,50,5])
X.append([50,70,50,5])
X.append([50,80,50,5])
X.append([50,90,50,5])
X.append([50,100,50,5])

Y.append(220.0)
Y.append(200.0)
Y.append(180.0)
Y.append(160.0)
Y.append(140.0)
Y.append(120.0)
Y.append(100.0)
Y.append(80.0)
Y.append(80.0)
Y.append(70.0)
Y.append(50.0)




from sklearn import tree
#X = [[0, 0], [2, 2]]
#y = [0.5, 2.5]
clf = tree.DecisionTreeRegressor()
clf = clf.fit(X, Y)
print(clf.predict([[45,50,80,5]]))
#array([ 0.5])
