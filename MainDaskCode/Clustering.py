from dask_ml import cluster
from dask.distributed import Client, LocalCluster


def clustering(x, workers, clusters):
    dask_cluster = LocalCluster(n_workers=workers)
    client = Client(dask_cluster)
    km = cluster.KMeans(n_clusters=clusters, init_max_iter=2, oversampling_factor=10)
    km.fit(x)
    client.shutdown()
    return
