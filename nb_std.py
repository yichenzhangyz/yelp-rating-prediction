import numpy as np
import matplotlib.pyplot as plt
# ############ naive bayes ############
# sparseOutFile
RMSE_1 = np.array([1.0796295661012623, 1.0629205050237764, 1.067145725756328, 1.0942577392917996, 1.041345283755585])

# sparseWithoutStop
RMSE_2 = np.array([1.0607544484940894, 1.065363787633126, 1.0540398474441086, 1.0737783756436894, 1.0468046618161384])

# sparseWithStem
RMSE_3 = np.array([1.046709128650362, 1.0421132376090423, 1.0600943354249186, 1.072100741535048, 1.0538500842150178])

# # sparseWithReduce
# RMSE_4 = np.array([1.0757323087088162, 1.0597169433391165, 1.066770828247567, 1.0737783756436894, 1.105350623105628])

# # sparseMatrixWithBigram
# RMSE_5 = np.array([1.0572606112023657, 1.0489995233554685, 1.0533755265810953, 1.0539449701004318, 1.0861859877571611])

mean_rmse = []
std_rmse = []
for rmse in [RMSE_1, RMSE_2, RMSE_3,]:
	mean_rmse.append(np.mean(rmse))
	std_rmse.append(np.std(rmse))
print "mean of naive bayes datasets: " + str(mean_rmse)
print "std of naive bayes datasets: " + str(std_rmse)
iteration=[1,2,3]
plt.errorbar(iteration, mean_rmse, std_rmse, linestyle='-', marker='o')
plt.axis([0,4,0.8,1.2])


plt.show()

