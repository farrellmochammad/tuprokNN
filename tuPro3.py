from __future__ import division
from xlrd import open_workbook
from math import sqrt


wb = open_workbook('Dataset Tugas 3 AI 1718.xlsx')
value1 = []
value2 = []
value3 = []
value4 = []
value5 = []
for s in wb.sheets():
    for i in range(s.nrows):
         value1.append(s.cell(i,1).value)
         value2.append(s.cell(i,2).value)
         value3.append(s.cell(i,3).value)
         value4.append(s.cell(i,4).value)
         value5.append(s.cell(i,5).value)
Data = [value1 , value2 , value3 , value4 , value5]

#print Data[0][0],Data[1][0],Data[2][0],Data[3][0],Data[4][0]

def euclid(A,B):
    return sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2 + (A[2]-B[2])**2 + (A[3]-B[3])**2 )

def toForm(matrix,idx):
    temp = []
    for i in range(0,len(Data)):
        temp.append(matrix[i][idx])
    return temp

"""
def kNN(nilaiknn,index):
    temp = []
    for i in range(1,4001):
        temp.append(euclid(toForm(Data,index),toForm(Data,i)))
    j = 0
    matriks,matriksidx = [],[]
    while(j<=nilaiknn):
        matriks.append(min(temp))
        matriksidx.append(temp.index(min(temp)))
        temp.remove(min(temp))
        j = j + 1
    class1,class2 = 0,0
    for j in range(0,len(matriks)):
        if (Data[4][matriksidx[j]]==1):
            class1 += 1
        else:
            class2 += 1
    if class1>class2:
        return 1
    else:
        return 0
"""

def kNN(knn,index,matriks):
    temp = []
    j = 0
    for i in range(1,len(matriks)):
        temp.append(euclid(toForm(Data,index),toForm(Data,matriks[i])))
    mt,matriksidx = [],[]
    while(j<=knn):
        mt.append(min(temp))
        matriksidx.append(temp.index(min(temp)))
        temp.remove(min(temp))
        j = j + 1
    class1,class2 = 0,0
    for j in range(0,len(mt)):
        if (Data[4][matriksidx[j]]==1):
            class1 += 1
        else:
            class2 += 1
    if class1>class2:
        return 1
    else:
        return 0



def kfoldcross(matriks,k):
    true,iterasi = 0,0
    count = 1
    while (count<=4001):
        datatrain = []
        datatest = []
        for j in range(1,4001):
            if (j>count and j<=count+k):
                datatest.append(j)
            else:
                datatrain.append(j)
        for k in range(0,len(datatest)):
            if (Data[4][k]==kNN(51,k,datatrain)):
                true += 1
        iterasi += 1
        print "Nilai akurasi ke-",str(iterasi),":",true/len(datatest)
        count += k



true = 0

"""
for i in range(1001,2001):
    print "Learning data ke-",i,Data[4][i],
    if (Data[4][i]==kNN(101,i)):
        true += 1
"""

kfoldcross(Data,500)


"""
k,literasi = 0,0
temp = []
while (k<=3500):
    true = 0
    print "sedang loading"
    for i in range(1+k,500+k):
        if (Data[4][i]==kNN(51,i)):
            true += 1
    temp.append(true/500)
    literasi += 1
    print "Akurasi ke-",literasi
    k += 500
print temp"""

print "Nilai Akurasi = ",true/1000
