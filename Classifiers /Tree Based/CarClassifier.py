from sklearn import tree

#Top Speed, 0-100 Time
features = [[320, 4], [230, 6.2], [170, 9], [115, 11], [210, 6], [195, 7.5], [225, 6.9], [217, 6.6]]
feature_names = ["Topspeed", "0-100km/h Time"]

#0 = ecoCAr, 1 = SPortsCar, 2 = Supercar
labels = ["Supercar", "Sports Car", "Regular Car", "Regular Car", "Sports Car", "Sports Car", "Sports Car", "Sports Car"]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print clf.predict([[280, 2.1], [9000, 0], [144, 9]])

#Show decision tree as pdf (DISCLAIMED: THIS WAS OBTAINED FROM THE SKLEARN WEBSITE, THIS IS NOT MY CODE)
from sklearn.externals.six import StringIO  
import pydot 
dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=feature_names,  
                         class_names=labels,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = pydot.graph_from_dot_data(dot_data.getvalue())  
graph.write_pdf("CarClassifer.pdf") 