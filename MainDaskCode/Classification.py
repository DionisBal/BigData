from dask.distributed import Client, LocalCluster
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import joblib


def classification(x, y, workers):
    dask_cluster = LocalCluster(n_workers=workers)
    client = Client(dask_cluster)
    param_grid = {"C": [0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0],
                  "kernel": ['rbf', 'poly', 'sigmoid'],
                  "shrinking": [True, False]}

    grid_search = GridSearchCV(SVC(gamma='auto', random_state=0, probability=True),
                               param_grid=param_grid,
                               return_train_score=False,
                               cv=3,
                               n_jobs=-1)
    with joblib.parallel_backend('dask'):
        grid_search.fit(x, y)
        score = grid_search.score(x, y)
    client.shutdown()
    return score
