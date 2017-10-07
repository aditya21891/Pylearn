# this is a program to predict the gender using machine Learning 
# thanks to Siraj Raval 

#!/usr/bin/env python 

from sklearn import tree 

#[height,weight,shoe size]
x=[[180,145,7],[140,150,8],[155,170,10],[130,124,12],[220,140,11],[245,115,13],[250,145,14],[270,130,16]]
y=['male','female','male','female','male','female','male','female']

clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
predict=clf.predict([[200,155,10]])

print predict 

