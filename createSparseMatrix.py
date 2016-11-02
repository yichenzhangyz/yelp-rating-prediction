import csv
from scipy.sparse import coo_matrix
countData = []

with open('counts.txt', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        countData.append(row)
print len(countData)

rowCoo = []
colCoo = []
freq = []
for i in range (len(countData)):
    rowCoo.append(int(countData[i][0])-1)
    colCoo.append(int(countData[i][1])-1)
    freq.append(int(countData[i][2]))

countSparseMatrix = coo_matrix((freq, (rowCoo,colCoo)), shape = (25000, 56835))
print countSparseMatrix

strout = ""
from scipy.io import mmwrite
mmwrite('./sparseOutFile', countSparseMatrix, 'this is comment, hahaha')
print strout