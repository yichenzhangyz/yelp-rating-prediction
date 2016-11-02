
import csv

# from scipy.io import mmread
# countSpaMat = mmread('./sparseWithStem')

# from scipy.sparse import find
# (rowCoo, colCoo, counts) = find(countSpaMat)

from scipy.io import mmread
countSpaMat = mmread('./sparseWithReduce')  ######  change the name of final feature selection here

from scipy.sparse import find
(rowCoo, colCoo, counts) = find(countSpaMat)

bigramRowCoo = []
bigramColCoo = []
bigramCounts = []
for i in range (len(rowCoo)):
    bigramRowCoo.append(rowCoo[i])
    bigramColCoo.append(colCoo[i])
    bigramCounts.append(counts[i])



biGramVocArray = []

with open('bigramVocab.txt', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        biGramVocArray.append(row) 
print len(biGramVocArray)        
print biGramVocArray[2][0]
print biGramVocArray[2]




wholeMetaData = []
count =0
with open('train_metadata.txt', 'rb') as f2:
    reader2 = csv.reader(f2, delimiter='\t')
    for row in reader2:
        count += 1
        wholeMetaData.append(row)

# print len(wholeMetaData)

# print wholeMetaData[0][0]
# print wholeMetaData[0][1]
# print wholeMetaData[0][2]
# print wholeMetaData[0][3]
# print wholeMetaData[0][4]
# print wholeMetaData[0][5]
# print wholeMetaData[0][5][0]
# print wholeMetaData[0][5][1]



originalText = []
textReviewData = []
for i in range (25000):
    originalText = wholeMetaData[i][5]
    newText = originalText.split()
    textReviewData.append(newText)
print textReviewData[0][0]


with open('trainReviewText.txt', 'wb') as f3:
    writer = csv.writer(f3)
    for i in range (25000):
        writer.writerow(textReviewData[i])

# freqArray = [0] * len(biGramVocArray)
# print len(freqArray)
# print freqArray[0]

# a = biGramVocArray[0][0]
# b = biGramVocArray[1][0]
# c = a + b
# print c



def findBigram(oneReviewText):
    base1 = ['not', 'nothing']
    base2 = ['nota', 'notvery', 'nottoo']
    base3 = ['notavery']

    length = len(oneReviewText)

    freqArray = [0] * len(biGramVocArray)

    for i in range (len(oneReviewText)):
        matchBase1 = (oneReviewText[i] in base1)
        bigram = []
        if matchBase1 & ((i+1) < len(oneReviewText)):
            bigram = oneReviewText[i] + oneReviewText[i+1]
            matchBase2 = (bigram in base2)
            if matchBase2 & ((i+2) < len(oneReviewText)):
                bigram = bigram + oneReviewText[i+2]
                matchBase3 = (bigram in base3)
                if  matchBase3 & ((i+3) < len(oneReviewText)):
                    bigram = bigram + oneReviewText[i+3]
        for j in range (len(biGramVocArray)):
            match = 0
            if bigram == biGramVocArray[j][0]:
                match = 1
                freqArray[j] += 1
                break
    return freqArray





reducedCol = countSpaMat.shape[1]

for i in range (25000):
    oneSampleBigramFreq = findBigram(textReviewData[i])
    for j in range (len(biGramVocArray)):
        if oneSampleBigramFreq[j]:
            print "sample" + str(i)
            print "has bigram" + str(j) + "of" + str(oneSampleBigramFreq[j])
            bigramRowCoo.append(i)
            bigramColCoo.append(j+reducedCol)#######change to the number of final matrix column number(after all feature selection)
            bigramCounts.append(oneSampleBigramFreq[j])



from scipy.sparse import coo_matrix
newColDim = reducedCol + len(biGramVocArray)

countSparseMatrixWithBigram = coo_matrix((bigramCounts, (bigramRowCoo,bigramColCoo)), shape = (25000, newColDim))

from scipy.io import mmwrite
mmwrite('./sparseMatrixWithBigram', countSparseMatrixWithBigram, 'this is comment, hahaha')





