# this is my first amchine learning program in python 
# thanks to JB Gordon 

#!usr/bin/env python 

from sklearn import tree 

features=[[140,1],[130,1],[150,0],[170,0]]
labels=[0,0,1,1]

clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print clf.predict([[160,0]])
print clf.predict([[120,0]]) 

