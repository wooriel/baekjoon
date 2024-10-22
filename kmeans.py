
# make a k-means program

import numpy as np
from sklearn.cluster import KMeans

# Create an array of points with x and y coordinates
points = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# Create a KMeans object with 2 clusters 
kmeans = KMeans(n_clusters=2)

# Fit the points to the model 
kmeans.fit(points) 

# Get the cluster labels 
labels = kmeans.predict(points) 
print(labels)