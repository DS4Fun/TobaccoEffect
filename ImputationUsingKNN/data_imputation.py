import sys
import numpy as np
from numpy import genfromtxt
from impyute.imputation.cs import fast_knn
import pandas as pd

# with open('Tobacco_cost.csv') as file:
#     d = file.read().replace("\"", "")
#     # file.write(d)
#     file1 = open("testfile.txt", "w")
#     file1.write(d)
#     my_data = genfromtxt(file1, delimiter=',')

# my_data_1 = pd.read_csv('testfile.csv')
my_data_2 = pd.read_csv('Tobacco_cost.csv')
my_data_2 = my_data_2.drop(['Country'], axis=1)

# my_np_array_2 = np.array(my_data_2)
# my_np_array_2_changes = np.delete(np.delete(my_np_array_2, 0, 0), [0,2],1)
# # my_np_array_2.astype('int32').dtypes
# my_data_2.apply(lambda x: pd.to_numeric(x, errors='force'))

# for i in range(np.size(my_np_array_2_changes,0)):
#     for j in range(np.size(my_np_array_2_changes,1)):
#         if type(my_np_array_2_changes[i][j]) == str:
#             my_np_array_2_changes[i][j] = float(my_np_array_2_changes[i][j])
#             print("Hello")

# for x in np.nditer(my_np_array_2):
#     if type(x) == str:
#         print("Hello")



# # my_data = genfromtxt('testfile.csv', delimiter=',')
# # my_data = np.delete(np.delete(my_data, 0, 0), [0,2],1)
# # imputed_training=fast_knn(my_data, k=3)


# my_data1 = genfromtxt('tobacco_use_missing_copy.csv', delimiter=',')
# my_data1 = np.delete(np.delete(my_data1, 0, 0), 1, 1)
# #
# # sys.setrecursionlimit(100000) #Increase the recursion limit of the OS
# # # start the KNN training
# imputed_training=fast_knn(my_data1, k=30)
# # df = my_data_1.assign(B=df1['E'])
# # imputed_training[:,1]
# print(imputed_training)