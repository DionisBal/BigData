from dask_ml.linear_model import LinearRegression
from dask_ml.metrics import accuracy_score
from dask.distributed import Client, LocalCluster
import subprocess


def linear_regression(x_train, y_train, x_test, y_test):
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    y_pred = lr.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy
