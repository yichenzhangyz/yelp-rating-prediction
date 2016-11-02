from scipy.io import mmread
countSpaMat = mmread('./sparseWithStem')

from scipy.sparse import find
(rowCoo, colCoo, counts) = find(countSpaMat)

print rowCoo
print colCoo
print counts

voc_array = []

f2 = open("new_vocab_with_stem.txt","rb")
lines = f2.readlines()
for i in range(0, len(lines)):
    l = lines[i]
    word = l[0:len(l) - 1]
    # print word
    voc_array.append(word)
# print voc_array

# calculate total counts of each column
col_counts = {}
for i in range(len(colCoo)):
    if colCoo[i] not in col_counts:
        col_counts[colCoo[i]] = counts[i]
    else:
        col_counts[colCoo[i]] += counts[i]
# print col_counts

remove_set = set()
new_voc_array = []
new_voc_dict = {}
voc_index = 0
for i in range(len(voc_array)):
    if i in col_counts:
        freq = col_counts[i]/float(25000)
    else:
        freq = 0
    if freq < 0.0005:
        # add index of vocab array to be remove in a set
        remove_set.add(i)
    else:
        new_voc_array.append(voc_array[i])
        # record he new vocab array's column number
        new_voc_dict[voc_array[i]] = voc_index
        voc_index += 1

new_rowCoo = []
new_colCoo = []
new_counts = []

current_row = -1
newvoc_to_counts = {}

# reduce the matrix dimension row by row
row_size = len(rowCoo)
for i in range (row_size):
    row = rowCoo[i]
    # print "current row is " + str(row)
    # now analyze a new row.
    if row > current_row:
        for key, value in newvoc_to_counts.iteritems():
            new_rowCoo.append(current_row)
            new_colCoo.append(new_voc_dict[key])
            new_counts.append(value)
        current_row += 1
        newvoc_to_counts = {}

    cur_column = colCoo[i]
    if cur_column not in remove_set:
        newvoc_to_counts[voc_array[cur_column]] = counts[i]

for key, value in newvoc_to_counts.iteritems():
    new_rowCoo.append(row)
    new_colCoo.append(new_voc_dict[key])
    new_counts.append(value)

# print new_voc_array
print len(new_voc_array)

f3 = open("new_vocab_reduce_sparse.txt","w")
for item in new_voc_array:
    # print item
    f3.write(item)
    f3.write("\n")

from scipy.sparse import coo_matrix
countSparseMatrixWithStem = coo_matrix((new_counts, (new_rowCoo,new_colCoo)), shape = (25000, len(new_voc_array)))


strout = ""
from scipy.io import mmwrite
mmwrite('./sparseWithReduce', countSparseMatrixWithStem, 'this is comment, hahaha')
print strout

 


