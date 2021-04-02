import pandas as pd
import numpy as np
import math

breast_data = pd.read_csv("breast_data.csv", header=None)
BD = (breast_data.iloc[:,:].values)

breast_truth = pd.read_csv("breast_truth.csv", header=None)
BT = (breast_truth.iloc[:].values)

centroid_number = 2
centroids = []

for i in range(centroid_number):
    centroids.append(BD[np.random.randint(1,570)])


for i in range(10):
    
    cluster1 = []
    cluster2 = []

    for data in range(569):
        a = 0
        b = 0
        for i in range(30):
            a = a + (BD[data][i] - centroids[0][i])**2
            b = b + (BD[data][i] - centroids[1][i])**2

        if np.sqrt(a)<np.sqrt(b):
            cluster1.append(BD[data])
        else:
            cluster2.append(BD[data])

    new_centroid1 = np.mean(cluster1, axis=0)
    new_centroid2 = np.mean(cluster2, axis=0)

    centroids = []
    centroids.append(new_centroid1)
    centroids.append(new_centroid2)

    new_cluster1 = []
    new_cluster2 = []

    predictions = []

    for data in range(569):
        a = 0
        b = 0
        for i in range(30):
            a = a + (BD[data][i] - new_centroid1[i])**2
            b = b + (BD[data][i] - new_centroid2[i])**2

        if np.sqrt(a)<np.sqrt(b):
            new_cluster1.append(BD[data])
            predictions.append(0)
            
        else:
            new_cluster2.append(BD[data])
            predictions.append(1)

    print(len(new_cluster1))
    print(len(new_cluster2))
    #print(predictions)

    sum = 0
    for i in range(569):
        if BT[i] == predictions[i]:
            sum += 1
        
    print(f"Accuracy: %{sum/569 * 100}")
