from sklearn import tree
import pandas as pd
from sklearn.datasets import load_iris
import numpy as np
import graphviz 

#cross-validation ARAŞTIR

newdata=pd.read_csv('newdata.csv')  # BIR CSV DOSYASI OKUDUK
onur=newdata.fillna(value=5)
matrix=onur.to_numpy() # PANDAS'I NUMPY MATRISINE CEVIRDIK.
X=matrix[:, 2:]  # BURADA MATRİSİN 0-4 ARASINI ALDIK
Y=matrix[:,1]   #BURADA MATRİSİN SADECE 4.SÜTUNUNU ALDIK

_data=[]

_data.extend(matrix[0:600,1])

_test=[]
_test.extend(matrix[0:600,2:])

clf = tree.DecisionTreeClassifier()  # ağaç sınıflandırması
clf = clf.fit(X, Y)                 # ağaç öğretimi
deneme_class=clf.predict(_test)    # class ile ilgili tahminler

#print(deneme_class)


from sklearn.metrics import confusion_matrix


y_true = _data  # gerçek veri class
y_pred = deneme_class   # tahmini class
print(confusion_matrix(y_true, y_pred))

from sklearn.metrics import classification_report

target_names = ['Sınıf1', 'class 1', 'class 2'] # rapordaki sınıfların isimleri

print(classification_report(y_true, y_pred))
