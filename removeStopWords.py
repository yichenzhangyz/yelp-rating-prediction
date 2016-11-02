
import csv

from scipy.io import mmread
countSpaMat = mmread('./sparseOutFile')

from scipy.sparse import find
(rowCoo, colCoo, counts) = find(countSpaMat)

# print counts[0]



stopWordArray = []
with open('stopwords.txt', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        stopWordArray.append(row)  ###since the txt file only contains one line, so this is a length 1 array, and the 1st line contains all stop words

print stopWordArray[0][0]




wholeVocArray = []

with open('vocab.txt', 'rb') as f2:
    reader2 = csv.reader(f2)
    for row in reader2:
        wholeVocArray.append(row) 
# print len(wholeVocArray) ### this is a length of 56835 array, each line is a list eg ['a'], to get the pure string, should use two indices[i][0]
print wholeVocArray[1409][0]




removeIndex = []
for i in range (len(wholeVocArray)):
    if wholeVocArray[i][0] in stopWordArray[0]:
        for j in range (len(colCoo)):
            if colCoo[j] == i:
                removeIndex.append(j)
print len(removeIndex)
removeIndex.sort()


newRowCoo = []
newColCoo = []
newCounts = []

j = 0
for i in range (len(rowCoo)):
    if j < len(removeIndex):
        if i < removeIndex[j]:
            newRowCoo.append(rowCoo[i])
            newColCoo.append(colCoo[i])
            newCounts.append(counts[i])
        elif i == removeIndex[j]:
            j += 1
    else:
        newRowCoo.append(rowCoo[i])
        newColCoo.append(colCoo[i])
        newCounts.append(counts[i])
print len(newRowCoo)
print len(newColCoo)
print len(newCounts)



newRowDim = len(wholeVocArray) - len(stopWordArray[0])

from scipy.sparse import coo_matrix
countSparseMatrixWithoutStop = coo_matrix((newCounts, (newRowCoo,newColCoo)), shape = (25000, 56835))


from scipy.io import mmwrite
mmwrite('./sparseWithoutStop', countSparseMatrixWithoutStop, 'this is comment, hahaha')



            
                



