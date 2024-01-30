import ray
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import joblib
from ray.util.joblib import register_ray
import time


def ray_classification(workers):
    digits = load_digits()

    param_grid = {"C": [0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0],
                  "kernel": ['rbf', 'poly', 'sigmoid'],
                  "shrinking": [True, False]}

    grid_search = GridSearchCV(SVC(gamma='auto', random_state=0, probability=True),
                               param_grid=param_grid,
                               return_train_score=False,
                               cv=3,
                               n_jobs=workers)
    register_ray()

    with joblib.parallel_backend('ray'):
        start_time = time.time()
        grid_search.fit(digits.data, digits.target)
        execution_time = time.time()-start_time

    ray.shutdown()
    return execution_time
