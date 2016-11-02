import csv
import math
from scipy import sparse
from sklearn import svm
from scipy.io import mmread
from sklearn.cross_validation import train_test_split
import numpy as np
import time
from collections import Counter

# random split data
# if want to randomly split data without seed, delete random_state = 4  in train_test_split()
# if need the experiment repeatable, add random_state = ? in train_test_split()
def split_data(data, label, ratio, random_seed):
	x_train, x_test, y_train, y_test = train_test_split(data, label, test_size = ratio, random_state = random_seed)
	return x_train, x_test, y_train, y_test


def cal_rmse(predictArray, y):
	RMSE = 0
	error = 0.0
	for i in range (len(y)):
	    error += float(((predictArray[i]) - y[i]) * (float(predictArray[i]) - y[i]))
	    # print "error after " + str(i) + " is " + str(error)
	error = error/len(y)
	RMSE = math.sqrt(error)
	return RMSE

def svm_train(X_train, y_train, X_test, c):
	
	clf = svm.SVC(C = c, kernel = "linear")
	clf.fit(X_train, y_train)  
	# predictArray = []
	predictArray = clf.predict(X_test)
	return predictArray

def find_vote(array):
	count = Counter(array)
	vote = count.most_common(1)[0][0]
	return vote

def avg_model(X_train, X_test, y_train, y_test, c, start, stop):
	predict_y = np.array([10]*len(y_test))
	rmse_array = []
	# time1=time.time()
	for index in range(start, stop):
		x_trn, x_drop, y_trn, y_drop = split_data(X_train, y_train, 0.4, index)
		temp_predict_y = np.array(svm_train(x_trn, y_trn, X_test, c))
		predict_y = np.column_stack((predict_y, temp_predict_y))
		print "predict_y shape is:" + str(predict_y.shape) + "when the " + str(index) + "th iteration"
	# time2=time.time()
	# print "time used:" + str(time2-time1)
		
		final_pred_y=[]
		for i in range(predict_y.shape[0]):
			cur_row = predict_y[i][1:]
			vote = find_vote(cur_row)
			final_pred_y.append(vote)
		print "final_pred_y shape is:" + str(len(final_pred_y))
		rmse = cal_rmse(final_pred_y, y_test)
		rmse_array.append(rmse)
		print "RMSE list: " + str(rmse_array)
		print "====================="
	return rmse_array

file_name = './sparseWithReduce'
countSpaMat = mmread(file_name)
X = countSpaMat.tocsr()

# process y
label = []
with open('labels.txt', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        label.append(row) 
y = []
for i in range (len(label)):
    y.append(int(label[i][0]))


for i in range(4):
	print "====== the " + str(i) + "th iteration ======="
	X_train, X_test, y_train, y_test = split_data(X, y, 0.2, i)
	c = 0.05
	rmse_list = []
	start = 0
	stop = 50
	# print "when there are total " + str(iter_num) + " iterations"
	rmse_list = avg_model(X_train, X_test, y_train, y_test, c, start, stop)
	# rmse_list.append(rmse)
	print "rmse list is: " + str(rmse_list)

