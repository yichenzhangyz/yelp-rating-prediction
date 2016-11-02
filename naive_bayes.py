import csv
import math
from scipy import sparse
from sklearn.naive_bayes import MultinomialNB
from scipy.io import mmread



def nb_rmse(file_name):
	# read sparse matrix into X
	countSpaMat = mmread(file_name)
	X = countSpaMat.tocsr()
	X = X.toarray()
	
	# make y from labels.txt
	label = []
	with open('labels.txt', 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	        label.append(row) 
	y = []
	for i in range (len(label)):
	    y.append(int(label[i][0]))


	# multinomial naive bayes
	mu_nb = MultinomialNB()
	y_pred = mu_nb.fit(X[:20000], y[:20000]).predict(X[-5000:])

	RMSE = 0
	error = 0.0

	for i in range (5000):
	    error += float(((y_pred[i]) - y[20000 + i]) * (float(y_pred[i]) - y[20000 + i]))
	error = error/5000
	print "error of Multinomial Naive Bayes is " + str(error) + " with file " + file_name
	RMSE = math.sqrt(error)
	print "RMSE of Multinomial Naive Bayes is " + str(RMSE) + " with file " + file_name
	return RMSE

file_name_1 = "./sparseOutFile"
file_name_2 = "./sparseWithoutStop"
file_name_3 = "./sparseWithStem"
file_name_4 = './sparseWithReduce'
file_name_5 = "./sparseMatrixWithBigram"


nb_rmse(file_name_1)
nb_rmse(file_name_2)
nb_rmse(file_name_3)
nb_rmse(file_name_4)
nb_rmse(file_name_5)

