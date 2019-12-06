# İRİSİ ÇEKTİKTEN SONRA SATIRLARI VE SÜTUNLARI İSTEKLERİN DOĞRULTUSUNDA SINIFLANDIRIYORSUN
# SINIFLANDIRMADAN SONRA BUNLARI TEST DATA VB ISIMLERLE ÇEKİYORSUN VE DAHA SONRADAN
# BUNLARI MAKİNE ÖĞRENMESİ İLE ÖRĞRETYORSUN ÖĞRETTİKTEN SONRA
# confusion_matrix YARDIMIYLA ÇIKTILARI KARŞILAŞTIRIYORSUN
# confusion_matrix ÇIKTISINDAN SONRA CLASSİFİCATİON_MATRİX İLE BUNUN RAPORUNU ALIYORSUN

from sklearn import tree
import pandas as pd
from sklearn.datasets import load_iris
import numpy as np
import graphviz 



iris=pd.read_csv('iris.csv')  # BIR CSV DOSYASI OKUDUK

matrix=iris.to_numpy() # PANDAS'I NUMPY MATRISINE CEVIRDIK.
X=matrix[:, 0:4]  # BURADA MATRİSİN 0-4 ARASINI ALDIK
Y=matrix[:,4]   #BURADA MATRİSİN SADECE 4.SÜTUNUNU ALDIK



iris=load_iris()


_data=[]
_data.extend(matrix[0:40,0:4])
_data.extend(matrix[50:90,0:4])
_data.extend(matrix[100:140,0:4])


_test=[]
_test.extend(matrix[40:50,0:4])
_test.extend(matrix[90:100,0:4])
_test.extend(matrix[140:150,0:4])

_class_pred=[]                              # Buradaki verilerin sınıfları
_class_pred.extend(matrix[40:50,4])
_class_pred.extend(matrix[90:100,4])
_class_pred.extend(matrix[140:150,4])

_class_data=[]
_class_data.extend(matrix[0:40,4])
_class_data.extend(matrix[50:90,4])
_class_data.extend(matrix[100:140,4])



clf = tree.DecisionTreeClassifier()  # ağaç sınıflandırması
clf = clf.fit(X, Y)                 # ağaç öğretimi
deneme_class=clf.predict(_test)    # class ile ilgili tahminler


from sklearn.metrics import confusion_matrix


y_true = _class_pred  # gerçek veri class
y_pred = deneme_class   # tahmini class
print(confusion_matrix(y_true, y_pred))


from sklearn.metrics import classification_report

target_names = ['Sınıf1', 'class 1', 'class 2'] # rapordaki sınıfların isimleri

print(classification_report(y_true, y_pred, target_names=target_names)) #burada class osnucunu yazdırıyotuz
