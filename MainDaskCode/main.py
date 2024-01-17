from dask_ml.datasets import make_regression
from dask_ml.linear_model import LinearRegression
from dask_ml.model_selection import train_test_split
from dask.distributed import Client, LocalCluster
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cluster = LocalCluster(n_workers=8)
    client = Client(cluster)

    for nanny in cluster.workers.values():
        port = nanny.listen_address.split(':')[2]
        print(port)
        # initiate measurements for each port

    X, y = make_regression(n_samples=1000000, n_features=500, chunks=500)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3, convert_mixed_types=True)
    lr = LinearRegression()
    start_time = time.time()
    lr.fit(X_train, y_train)
    execution_time = time.time() - start_time
    y_pred = lr.predict(X_test)
    print(execution_time)
    client.shutdown()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
