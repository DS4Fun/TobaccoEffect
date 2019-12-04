import sys
import numpy as np
from numpy import genfromtxt
from impyute.imputation.cs import fast_knn

my_data = genfromtxt('tobacco_use_missing_copy.csv', delimiter=',')
my_data = np.delete(np.delete(my_data, 0, 0), 1, 1)
sys.setrecursionlimit(100000) #Increase the recursion limit of the OS
# start the KNN training
imputed_training=fast_knn(my_data, k=30)
print(imputed_training)