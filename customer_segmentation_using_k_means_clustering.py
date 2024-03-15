# -*- coding: utf-8 -*-
"""customer segmentation using k-means clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wj6upQDkEGLIDDmSztypzkShB2535cXe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# loading the data from csv file to a Pandas DataFrame
customer_data = pd.read_csv('/content/Mall_Customers.csv')

# first 5 rows in the dataframe
customer_data.head()

# finding the number of rows and columns
customer_data.shape

# getting some informations about the dataset
customer_data.info()

# checking for missing values
customer_data.isnull().sum()

X = customer_data.iloc[:,[3,4]].values

print(X)

# finding wcss value for different number of clusters

wcss = []

for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42, n_init=10)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

# plot an elbow graph

sns.set()
plt.plot(range(1,11), wcss)
plt.title('The Elbow Point Graph')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

"""Optimum Number of Clusters = 5

Training the k-Means Clustering Model
"""

kmeans=KMeans(n_clusters=5, init='k-means++', random_state=0, n_init=10)
# return a label for each data point based on their cluster
Y=kmeans.fit_predict(X)
print(Y)

"""5 Clusters - 0, 1, 2, 3, 4"""

# plotting all the clusters and their Centroids
plt.figure(figsize=(8,8))
plt.scatter(X[Y==0,0], X[Y==0,1], s=50, c='green', label='Cluster 1')
plt.scatter(X[Y==1,0], X[Y==1,1], s=50, c='red', label='Cluster 2')
plt.scatter(X[Y==2,0], X[Y==2,1], s=50, c='yellow', label='Cluster 3')
plt.scatter(X[Y==3,0], X[Y==3,1], s=50, c='violet', label='Cluster 4')
plt.scatter(X[Y==4,0], X[Y==4,1], s=50, c='blue', label='Cluster 5')

# plot the centroids
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='cyan', label='Centroids')
plt.title('Customer Groups')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()

