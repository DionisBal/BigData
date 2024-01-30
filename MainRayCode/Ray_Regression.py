from sklearn.linear_model import LinearRegression
import joblib
from ray.util.joblib import register_ray


def ray_regression(x_train, y_train, x_test, y_test):
    register_ray()
    with joblib.parallel_backend('ray'):
        lr = LinearRegression()
        lr.fit(x_train, y_train)
        y_pred = lr.predict(x_train)
    return 0
