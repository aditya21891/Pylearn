# this program is to test the data of iris flower data set.

from sklearn import datasets 
iris=datasets.load_iris()

x=iris.data 
y=iris.target 

from sklearn.cross_validation import train_test_split

x_train,y_train,x_test,y_test=train_test_split(x,y,test_size=0.5)

from sklearn import tree 
my_classifier=tree.DecisionTreeClassifier()

my_classifier.fit(x_train,y_train)

predict=my_classifier.predict(x_test)

from sklearn.metrics import accuracy_score

print accuracy_score(y_train,predict)

 
