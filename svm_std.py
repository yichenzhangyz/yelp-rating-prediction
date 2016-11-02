
import numpy as np
import matplotlib.pyplot as plt

# sparseOutFile
rmse_1 = np.array([0.9773433378296493, 0.9985990186255943, 0.9834632682515397, 0.9928746144403129, 0.9863062404750362, 0.9759098319004682, 0.9852918349402882, 0.9992997548283498, 0.9747820269167872, 1.0031948963187562])

# sparseWithoutReduce
rmse_2 = np.array([0.9941830817309254, 0.9941830817309254, 0.9834632682515397, 1.0257680049601858, 0.9702576977277738, 0.9802040603874277, 0.9932774033471213, 1.008265837961398, 0.9830564581955606, 0.9920685460188726])

# sparseMatrixWithBigram
rmse_3 = np.array([0.9916652661054536, 0.9898484732523458, 0.9876234100101111, 1.0254754994635416, 0.968607247546703, 0.9849873095629201, 0.9970957827611147, 0.9944847912361455, 0.9834632682515397, 0.9877246579892597])


mean_rmse = []
std_rmse = []
for rmse in [rmse_1, rmse_2, rmse_3,]:
	mean_rmse.append(np.mean(rmse))
	std_rmse.append(np.std(rmse))
print "mean of svm datasets: " + str(mean_rmse)
print "std of svm datasets: " + str(std_rmse)

plt.errorbar([1,2,3], mean_rmse, std_rmse, linestyle='-', marker='o')
plt.axis([0,4,0.8,1.2])

plt.show()


# Now read in ./sparseOutFile
# ========== ./sparseOutFile=============
# (25000, 56835)
# =========== 20th iteration =============
# RMSE of SVM is 0.9759098319 with file ./sparseOutFile
# =========== 21th iteration =============
# RMSE of SVM is 0.98529183494 with file ./sparseOutFile
# =========== 22th iteration =============
# RMSE of SVM is 0.999299754828 with file ./sparseOutFile
# =========== 23th iteration =============
# RMSE of SVM is 0.974782026917 with file ./sparseOutFile
# =========== 24th iteration =============
# RMSE of SVM is 1.00319489632 with file ./sparseOutFile
# [0.9759098319004682, 0.9852918349402882, 0.9992997548283498, 0.9747820269167872, 1.0031948963187562]
# #################
# Now read in ./sparseWithReduce
# ========== ./sparseWithReduce=============
# (25000, 6518)
# =========== 20th iteration =============
# RMSE of SVM is 0.980204060387 with file ./sparseWithReduce
# =========== 21th iteration =============
# RMSE of SVM is 0.993277403347 with file ./sparseWithReduce
# =========== 22th iteration =============
# RMSE of SVM is 1.00826583796 with file ./sparseWithReduce
# =========== 23th iteration =============
# RMSE of SVM is 0.983056458196 with file ./sparseWithReduce
# =========== 24th iteration =============
# RMSE of SVM is 0.992068546019 with file ./sparseWithReduce
# [0.9802040603874277, 0.9932774033471213, 1.008265837961398, 0.9830564581955606, 0.9920685460188726]
# #################
# Now read in ./sparseMatrixWithBigram
# ========== ./sparseMatrixWithBigram=============
# (25000, 10004)
# =========== 20th iteration =============
# RMSE of SVM is 0.984987309563 with file ./sparseMatrixWithBigram
# =========== 21th iteration =============
# RMSE of SVM is 0.997095782761 with file ./sparseMatrixWithBigram
# =========== 22th iteration =============
# RMSE of SVM is 0.994484791236 with file ./sparseMatrixWithBigram
# =========== 23th iteration =============
# RMSE of SVM is 0.983463268252 with file ./sparseMatrixWithBigram
# =========== 24th iteration =============
# RMSE of SVM is 0.987724657989 with file ./sparseMatrixWithBigram
# [0.9849873095629201, 0.9970957827611147, 0.9944847912361455, 0.9834632682515397, 0.9877246579892597]
