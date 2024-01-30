from dask_ml import cluster
from dask.distributed import Client, LocalCluster


def clustering(x, workers, clusters):
    km = cluster.KMeans(n_clusters=clusters, init_max_iter=2, oversampling_factor=10)
    km.fit(x)
    return
