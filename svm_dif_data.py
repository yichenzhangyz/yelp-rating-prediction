import csv
import math
from scipy import sparse
from sklearn import svm
from scipy.io import mmread
from sklearn.cross_validation import train_test_split

def cal_rmse(predictArray, y):
	RMSE = 0
	error = 0.0
	for i in range (len(y)):
	    error += float(((predictArray[i]) - y[i]) * (float(predictArray[i]) - y[i]))
	    # print "error after " + str(i) + " is " + str(error)
	error = error/len(y)
	RMSE = math.sqrt(error)
	return RMSE

def svm_rmse(X_train, X_test, y_train, y_test, c):
	clf = svm.SVC(C = c, kernel="linear")
	svc = clf.fit(X_train, y_train)  
	# predictArray = []
	# print svc
	predictArray = clf.predict(X_test)
	rmse = cal_rmse(predictArray, y_test)
	return rmse

# random split data
# if want to randomly split data without seed, delete random_state = 4  in train_test_split()
# if need the experiment repeatable, add random_state = ? in train_test_split()

def split_data(data, label, ratio, seed):
	x_train, x_test, y_train, y_test = train_test_split(data, label, test_size = ratio, random_state = seed)
	return x_train, x_test, y_train, y_test

def main(file_name):
	print "========== " + str(file_name) + "============="
	countSpaMat = mmread(file_name)
	X = countSpaMat.tocsr()

	print X.shape

	# process y
	label = []
	with open('labels.txt', 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	        label.append(row) 
	y = []
	for i in range (len(label)):
	    y.append(int(label[i][0]))
	rmse_list = []
	for i in range(20,25):
		print "=========== " + str(i) + "th iteration ============="
		X_train, X_test, y_train, y_test = split_data(X, y, 0.2, i)
		rmse = svm_rmse(X_train, X_test, y_train, y_test, 0.05)
		print "RMSE of SVM is " + str(rmse) + " with file " + file_name
		rmse_list.append(rmse)
	print rmse_list

file_name_1 = "./sparseOutFile"
# file_name_2 = "./sparseWithoutStop"
# file_name_3 = "./sparseWithStem"
file_name_4 = './sparseWithReduce'
file_name_5 = "./sparseMatrixWithBigram"


print "Now read in " + file_name_1
main(file_name_1)
print "#################"
# print "Now read in " + file_name_2
# main(file_name_2)
# print "#################"
# print "Now read in " + file_name_3
# main(file_name_3)
# print "#################"
print "Now read in " + file_name_4
main(file_name_4)
print "#################"
print "Now read in " + file_name_5
main(file_name_5)

