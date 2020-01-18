Many datasets we use for our data science tasks contain missing values. 
As each entity in our dataset can potentially represent important information, we can’t simply remove entities with missing values. There are different ways to deal with this missing values and replace them with some other numeric values, which are called data imputation strategies. One of the most effective way is imputation using KNN (K nearest neighbors). 
KNN constructs a KDTree and then looks for the k nearest neighbor of each node with a missing value. The weighted average of mentioned neighbors will be assigned to that node, as its value.