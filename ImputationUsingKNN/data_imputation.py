import sys
import numpy as np
from numpy import genfromtxt
from impyute.imputation.cs import fast_knn
import pandas as pd

#####
# 1. removing all the double quotes " from the entries. Because their type shouldn't be String.
# 2. fast_knn() admits np-array as input. So there is to way. Read the file as a csv file and then convert it to np-array,
# or read the file as a np-array at first.
# 3. note that when files are converted to np-array, all of their entries should be numeric(float) not String.
# The main problem we face here is that there are some methods that apparently give us a numeric array. But then all
# the entries are String, which are not admittable by fast_knn()
#####


#This part is done in the script "read_csv.py"
# with open('Tobacco_cost.csv') as file:
#     d = file.read().replace("\"", "")
#     # file.write(d)
#     file1 = open("testfile.txt", "w")
#     file1.write(d)


#First approach is reading the file as panda dataframe, with pd.read.csv()
#We get the cleaned csv file(without double quotes)
# my_data_1 = pd.read_csv('testfile.csv')

#we get the original csv file (it contain double quotes for all entries)
my_data_2 = pd.read_csv('Tobacco_cost.csv')
my_data_2 = my_data_2.drop(['Country'], axis=1) #droping the country column from the file because fast_knn() just works on numeric data

my_np_array_2 = np.array(my_data_2) #converting the panda dataframe to a np-array
my_np_array_2_changes = np.delete(np.delete(my_np_array_2, 0, 0), [0,2],1) #deleting the row and the columns which include String values
# my_np_array_2.astype('int32').dtypes  #trying to change the type of all columns of the np-array from String to float, which doesn't work
#my_data_2.apply(lambda x: pd.to_numeric(x, errors='force')) #Again trying to change the type of all columns of the np-array from String to float, which doesn't work again

#trying to loop over all the elements of np-array and change their type from String to float manually. This method also has problems with float(my_np_array_2_changes[i][j])
#when the values are not numeric but String
for i in range(np.size(my_np_array_2_changes,0)):
    for j in range(np.size(my_np_array_2_changes,1)):
        if type(my_np_array_2_changes[i][j]) == str:
            my_np_array_2_changes[i][j] = float(my_np_array_2_changes[i][j])

# for x in np.nditer(my_np_array_2):
#     if type(x) == str:
#         print("Hello")


#Second approach is reading the file as np-array, with genfromtxt()
my_data = genfromtxt('testfile.csv', delimiter=',') #reading the csv file as a np-array
my_data = np.delete(np.delete(my_data, 0, 0), [0,2],1) #deleting the columns which contain String values.
imputed_training=fast_knn(my_data, k=3) #applying fast-knn() on the np-array

#Here you can see the file which doesn't contain double quotes basically, and we haven't done any proceess on that to remove double quotes.
#This file fits fast-knn() and gives us the correct result.
my_data1 = genfromtxt('tobacco_use_missing_copy.csv', delimiter=',')
my_data1 = np.delete(np.delete(my_data1, 0, 0), 1, 1)
#
# sys.setrecursionlimit(100000) #Increase the recursion limit of the OS
# # start the KNN training
imputed_training=fast_knn(my_data1, k=30)
# df = my_data_1.assign(B=df1['E'])
# imputed_training[:,1]
print(imputed_training)