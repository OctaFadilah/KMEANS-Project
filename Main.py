## change "n" to the number you want

from sklearn.cluster import kmeans

n = 5
km = KMeans(n_clusters=n, random_state=42, n_init='auto')
km.fit(df)

target = km.labels_
print(target)

centroids = km.cluster_centers_
print (centroids)
