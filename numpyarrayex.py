import numpy as np



DIZI_BOYUTU=8 #dizi başlangıç noktası olarak 0 alınmıştır.
YENI_BOYUT=DIZI_BOYUTU-1 #n-1

temp=0

dizi1=[[1,0,0,0,0,1,0,1],[0,0,1,0,0,0,1,0],
[0,1,1,1,0,1,0,1],[0,0,1,0,0,0,0,1],
[0,0,0,0,1,1,0,0],[1,0,1,0,1,0,1,0],
[0,1,0,0,0,1,1,0],[1,0,1,1,0,0,0,0]]

dizi2=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

dizi3=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

dizi4=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0]]

print("\n Matrisin ilk hali: \n")

for i in range(DIZI_BOYUTU):
    for j in range(DIZI_BOYUTU):
        print(str(dizi1[i][j])+" ",end=' ')
    print()

print("\n Matris'in Tree Algoritması için ilk adımı ")

for i in range(DIZI_BOYUTU):
    for j in range(DIZI_BOYUTU):
        if i==j:
            for k in range(DIZI_BOYUTU):
                if dizi1[i][k]==1:
                    temp+=1
            dizi2[i][j]=temp
            temp=0
        else:
            dizi2[i][j]=dizi1[i][j]*(-1)
print()

for i in range(DIZI_BOYUTU):
    for j in range(DIZI_BOYUTU):
        if dizi2[i][j]>=0: print(str(dizi2[i][j])+" ",end='  ')
        else: print(str(dizi2[i][j])+" ",end=' ')
    print()

#DİZİDEN N-1 SATIRI SİLMEK İÇİN SATIRLARIN YERLERİNİ DEĞİŞTİRME İŞLEMİ
for i in range(DIZI_BOYUTU):
    for j in range(DIZI_BOYUTU):
        if i==6 and j==6:
            dizi3[i][j]=dizi2[i+1][j+1]
        elif i==6 and j!=6:
            dizi3[i][j]=dizi2[i+1][j]
        elif i!=6 and j==6:
            dizi3[i][j]=dizi2[i][j+1] 
        elif j==6:
            continue
        else:
            dizi3[i][j]=dizi2[i][j]

#DEĞİŞTİRİLEN SATIRI N-1 HALE GETİRMEK İÇİN ATAMA İŞLEMİ
for i in range(YENI_BOYUT):
    for j in range(YENI_BOYUT):
        dizi4[i][j]=dizi3[i][j]
        

print("\n Matris'in n-1 işlemi sonu oluşan yeni Matris: \n")
for i in range(YENI_BOYUT):
    for j in range(YENI_BOYUT):
        if dizi4[i][j]>=0: print(str(dizi4[i][j])+" ",end='  ')
        else: print(str(dizi4[i][j])+" ",end=' ')
    print()



matrisDeterminant = np.linalg.det(dizi4)


print("\n \n Matrisin determinantı: ",int(matrisDeterminant), "  olarak bulunur..!")
print()


