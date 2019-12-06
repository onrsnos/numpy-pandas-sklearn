from sklearn import tree
import pandas as pd
from sklearn.datasets import load_iris
import numpy as np
import graphviz 



iris=pd.read_csv('iris.csv')  # BIR CSV DOSYASI OKUDUK
matrix=iris.to_numpy() # PANDAS'I NUMPY MATRISINE CEVIRDIK.
X=matrix[:, 0:4]  # BURADA MATRİSİN 0-4 ARASINI ALDIK
Y=matrix[:,4]   #BURADA MATRİSİN SADECE 4.SÜTUNUNU ALDIK



clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
print(clf.predict([[2., 2.,2.,2.]]))   # TAHMIN ISLEMI


iris=load_iris()


dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("rastgele.txt")  # ismi verilen dosyaya yazıyor.


dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=iris.feature_names,  
                      class_names=iris.target_names,  
                  special_characters=True)  
graph = graphviz.Source(dot_data)  
print(graph)
import matplotlib.pyplot as plt
a=matrix[0,0:4]
print(a)