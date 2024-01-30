import ray

from dask_ml.linear_model import LinearRegression
from dask_ml import cluster
from dask_ml.datasets import make_regression
from dask_ml.model_selection import train_test_split
from ray.util.joblib import register_ray
from sklearn.datasets import make_regression, make_blobs
import joblib
import sklearn

import Classification
import Ray_Classification
import Ray_Regression
import dask_functions
import Regression
import time
import dask
import Dask_Loop
from ray.util.dask import ray_dask_get
from dask.distributed import Client, LocalCluster
from os import walk
import psutil
import dask.dataframe as dd
import dask.array as da
import subprocess
import numpy as np
import pandas as pd

def get_port_pid(port):
    connections = psutil.net_connections('tcp')
    for con in connections:
        if con.raddr != tuple():
            if con.raddr.port == port:
                return con.pid
        if con.laddr != tuple():
            if con.laddr.port == port:
                return con.pid
    return -1


@dask.delayed
def dask_parallel_loop(filename, save_path):
    return Dask_Loop.process_file(filename, save_path)


@ray.remote
def ray_parallel_loop(filename, save_path):
    Dask_Loop.process_file(filename, save_path)
    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # register_ray()
    # x_train_path = 'x_train/path.csv'
    # y_train_path = 'y_train/path.csv'
    #
    # x_test_path = 'x_test/path.csv'
    # y_test_path = 'y_test/path.csv'
    #
    # dfx_train = dask_functions.parallel_read(x_train_path)
    # dfy_train = dask_functions.parallel_read(y_train_path)
    #
    # dfx_test = dask_functions.parallel_read(x_test_path)
    # dfy_test = dask_functions.parallel_read(y_test_path)
    #
    # lr = LinearRegression()
    # start_time = time.time()
    # acc = Regression.linear_regression(dfx_train, dfy_train, dfx_test, dfy_test, 4)
    # execution_time = time.time() - start_time
    # print(execution_time)

    # cluster = LocalCluster(n_workers=2)
    # client = Client(cluster)
    #
    # for nanny in cluster.workers.values():
    #     port = nanny.listen_address.split(':')[2]
    #     print(port)

    filenames = []

    f = []
    for (dirpath, dirnames, filenames) in walk('E:\InformationSystemsData\data'):
        f.extend(filenames)
        break

    # results = []
    #
    # current_process = psutil.Process()
    #
    # children_start = current_process.children(recursive=True)
    #
    # context = ray.init(num_cpus=4)
    #
    # print(context.dashboard_url)

    # cl = LocalCluster(n_workers=8)
    # client = Client(cl)
    #
    # temp = []
    #
    # for nanny in cluster.workers.values():
    #     port = nanny.listen_address.split(':')[2]
    #     temp.append(port)
    #     print(port)

    # X_reg3, y_reg3 = make_regression(n_samples=1000000, n_features=500, chunks=500)

    # X, y = make_blobs(n_samples=1000000, n_features=1000)

    # X_train, X_test, y_train, y_test = train_test_split(X_reg3, y_reg3, test_size=0.33, random_state=42, shuffle=True)

    # lr = LinearRegression()

    # X_train = pd.read_csv("E:\InformationSystemsData\X_reg3.csv")
    # y_train = pd.read_csv("E:\InformationSystemsData\y_reg3.csv")

    # process_children = current_process.children(recursive=False)
    #
    # for child in process_children:
    #     if child.name() == "raylet.exe":
    #         ray_pid = child.pid
    #
    # ray_process = psutil.Process(ray_pid)
    #
    # ray_children = ray_process.children(recursive=False)
    #
    # ray_children_recursive = ray_process.children(recursive=True)
    #
    # temp = []
    # for child in ray_children_recursive:
    #     if child not in ray_children:
    #         temp.append(str(child.pid))

    # print(temp)
    #
    # ar = ['python.exe', '../ProcessMeasurements/main.py', '-pid']
    #
    # ar.extend(temp)
    #
    # subprocess.Popen(ar)

    # for filename in f:
    #     results.append(dask_parallel_loop(filename, r'E:\InformationSystemsData\results'))

    # ray.get(results)

    # dask.compute(results)

    # lr.fit(X_train, y_train)

    # lr = LinearRegression()

    # km = cluster.KMeans(n_clusters=2, init_max_iter=2, oversampling_factor=10, n_jobs=1)
    #
    # start_time = time.time()
    # km.fit(X)
    # execution_time = time.time() - start_time

    # with joblib.parallel_backend('ray', n_jobs=12):
    #     start_time = time.time()
    #     # lr.fit(X_train, y_train)
    #     km.fit(X)
    #     execution_time = time.time() - start_time
    #
    # lr = sklearn.linear_model.LinearRegression()
    # lr.fit(X_train, y_train)
    #

    start_time = time.time()

    # dfx_train = dask_functions.parallel_read(r"E:\InformationSystemsData\X_reg3.csv")

    x = ray.data.read_csv(r"E:\InformationSystemsData\X_reg3.csv", parallelism=12)

    # x = dd.read_csv(r"E:\InformationSystemsData\X_reg2.csv")

    print(x)

    execution_time = time.time() - start_time

    # acc = Regression.linear_regression(X_train, y_train, X_test, y_test, 4)
    # execution_time = Ray_Classification.ray_classification(1)
    # execution_time = Classification.classification(1)
    print(execution_time)

    # import ray_distributed

    # ray_distributed.distributed()

    # del results

    # client.shutdown()
    # ray.shutdown()
