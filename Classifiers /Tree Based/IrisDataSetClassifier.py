import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()

print iris.feature_names
print iris.target_names
print iris.data[0]

for i in range(len(iris.target)):
	print "Label: %s, Data: %s" % (iris.target[i], iris.data[i])

clf = tree.DecisionTreeClassifier();
clf = clf.fit(iris.data, iris.target)


print ("Setosa: 0, Versicolor: 1, Virginica: 2")
print clf.predict([[7.1,3.0,5.9,2.1]])

print iris.feature_names

#Show decision tree as pdf (DISCLAIMED: THIS WAS OBTAINED FROM THE SKLEARN WEBSITE, THIS IS NOT MY CODE)
from sklearn.externals.six import StringIO  
import pydot 
dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = pydot.graph_from_dot_data(dot_data.getvalue())  
graph.write_pdf("IrisDataSetClassifier.pdf") 