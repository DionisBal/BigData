import ray
from sklearn import cluster
import joblib
from ray.util.joblib import register_ray


def ray_clustering(x, workers, clusters):

    ray.init(num_cpus=workers, num_gpus=1)
    register_ray()

    with joblib.parallel_backend('ray'):
        km = cluster.KMeans(n_clusters=clusters, init_max_iter=2, oversampling_factor=10)
        km.fit(x)
    ray.shutdown()
    return
