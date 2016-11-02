
import csv

from scipy.io import mmread
countSpaMat = mmread('./sparseWithoutStop')

from scipy.sparse import find
(rowCoo, colCoo, counts) = find(countSpaMat)

from nltk.stem.porter import *

stemmer = PorterStemmer()

# print rowCoo
# print colCoo

wholeVocArray = []

with open('vocab.txt', 'rb') as f2:
    reader2 = csv.reader(f2)
    for row in reader2:
        wholeVocArray.append(row) 
print len(wholeVocArray) ### this is a length of 56835 array, each line just contain one word


new_voc_array = []


stem_set = set()
remove_set = set()
stem_voc_dict = {}
stem_voc_index = 0
for i in range(len(wholeVocArray)):
	voc = wholeVocArray[i]
	if len(voc) != 0:
		if voc[0].isalpha():
			origin = stemmer.stem(voc[0])
			if origin not in stem_set:
				stem_set.add(origin)
				stem_voc_dict[origin] = stem_voc_index
				stem_voc_index += 1
				# create new vocab array
				new_voc_array.append(voc[0])
				

			else:
				# record the index of the voc word to be removed.
				remove_index = i
				remove_set.add(remove_index)
	else:
		remove_set.add(i)


new_rowCoo = []
new_colCoo = []
new_counts = []

current_row = -1
stem_to_counts_dict = {}
row_size = len(rowCoo)
for i in range (row_size):
	row = rowCoo[i]
	# print "current row is " + str(row)
	# now analyze a new row.
	if row > current_row:
		if current_row != -1:
			# analysis of current_row finishes
			for key, value in stem_to_counts_dict.iteritems():
				new_rowCoo.append(current_row)
				new_voc_col = stem_voc_dict[key]
				new_colCoo.append(new_voc_col)
				new_counts.append(value)

		current_row += 1
		stem_to_counts_dict = {}
	
	# get the col_num
	voc_col_num = colCoo[i]
	# skip those empty words
	if len(wholeVocArray[voc_col_num]) == 0: 
		continue
	# get the word
	voc_word = wholeVocArray[voc_col_num][0]
	# print "voc word is " + str(voc_word)
	# skip non-alphbetic words
	if not voc_word.isalpha():
		continue
	# get the stem for the voc word
	stem_i = stemmer.stem(voc_word)
	# print "stem of voc word is " + str(stem_i)
	if stem_i not in stem_to_counts_dict:
		# if not in the dict, store it. Key is stem, value is counts
		stem_to_counts_dict[stem_i] = counts[i]
		# print "counts of new stem \"" + str(stem_i) + "\" is " + str(stem_to_counts_dict[stem_i])
	else:
		# if in the dict, add the counts to existing counts
		stem_to_counts_dict[stem_i] += counts[i]
		# print "counts of new stem \"" + str(stem_i) + "\" is " + str(stem_to_counts_dict[stem_i])

for key, value in stem_to_counts_dict.iteritems():
	new_rowCoo.append(current_row)
	new_voc_col = stem_voc_dict[key]
	new_colCoo.append(new_voc_col)
	new_counts.append(value)



f3 = open("new_vocab_with_stem.txt","w")
for item in new_voc_array:
	# print item
	f3.write(item)
	f3.write("\n")

from scipy.sparse import coo_matrix
countSparseMatrixWithStem = coo_matrix((new_counts, (new_rowCoo,new_colCoo)), shape = (25000, len(new_voc_array)))


strout = ""
from scipy.io import mmwrite
mmwrite('./sparseWithStem', countSparseMatrixWithStem, 'this is comment, hahaha')
print strout

      



		