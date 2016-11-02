import csv
import math
from scipy import sparse
from sklearn import svm
from scipy.io import mmread
from sklearn.cross_validation import train_test_split

# random split data
# if want to randomly split data without seed, delete random_state = 4  in train_test_split()
# if need the experiment repeatable, add random_state = ? in train_test_split()
def split_data(data, label, ratio):
	x_train, x_test, y_train, y_test = train_test_split(data, label, test_size = ratio, random_state = 20)
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

def cv_svm(X_train, X_test, y_train, y_test, c_grid):
	for c in c_grid:
		clf = svm.SVC(C = c, kernel = "linear")
		clf.fit(X_train, y_train)  
		# predictArray = []
		predictArray = clf.predict(X_test)
		rmse = cal_rmse(predictArray, y_test)
		print "when c is " + str(c) + ", RMSE is " + str(rmse)

file_name = './sparseMatrixWithBigram'
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

X_train, X_test, y_train, y_test = split_data(X, y, 0.2)

c_grid = [0.01, 0.05, 0.10, 0.50, 1.00, 1.20, 1.50, 2.00]
cv_svm(X_train, X_test, y_train, y_test, c_grid)
