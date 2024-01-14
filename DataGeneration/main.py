from dask_ml.datasets import make_regression
from dask_ml.datasets import make_blobs
from dask_ml.datasets import make_classification
import dask.dataframe as dd
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    X_reg1, y_reg1 = make_regression(n_samples=10000, n_features=1000, chunks=1000)
    dfx = dd.io.from_dask_array(X_reg1)
    dfy = dd.io.from_dask_array(y_reg1)
    dfx = dfx.compute()
    dfy = dfy.compute()
    dfx.to_csv(os.path.join('E:\InformationSystemsData', 'X_reg1.csv'))
    dfy.to_csv(os.path.join('E:\InformationSystemsData', 'y_reg1.csv'))
    del dfx
    del dfy
    del X_reg1
    del y_reg1

    X_blob1, y_blob1 = make_regression(n_samples=10000, n_features=1000, chunks=1000)
    dfx = dd.io.from_dask_array(X_blob1)
    dfy = dd.io.from_dask_array(y_blob1)
    dfx = dfx.compute()
    dfy = dfy.compute()
    dfx.to_csv(os.path.join('E:\InformationSystemsData', 'X_blob1.csv'))
    dfy.to_csv(os.path.join('E:\InformationSystemsData', 'y_blob1.csv'))
    del dfx
    del dfy
    del X_blob1
    del y_blob1

    X_class1, y_class1 = make_regression(n_samples=10000, n_features=1000, chunks=1000)
    dfx = dd.io.from_dask_array(X_class1)
    dfy = dd.io.from_dask_array(y_class1)
    dfx = dfx.compute()
    dfy = dfy.compute()
    dfx.to_csv(os.path.join('E:\InformationSystemsData', 'X_class1.csv'))
    dfy.to_csv(os.path.join('E:\InformationSystemsData', 'y_class1.csv'))
    del dfx
    del dfy
    del X_class1
    del y_class1

    X_reg2, y_reg2 = make_regression(n_samples=100000, n_features=1000, chunks=1000)
    dfx = dd.io.from_dask_array(X_reg2)
    dfy = dd.io.from_dask_array(y_reg2)
    dfx = dfx.compute()
    dfy = dfy.compute()
    dfx.to_csv(os.path.join('E:\InformationSystemsData', 'X_reg2.csv'))
    dfy.to_csv(os.path.join('E:\InformationSystemsData', 'y_reg2.csv'))
    del dfx
    del dfy
    del X_reg2
    del y_reg2

    X_blob2, y_blob2 = make_regression(n_samples=100000, n_features=1000, chunks=1000)
    dfx = dd.io.from_dask_array(X_blob2)
    dfy = dd.io.from_dask_array(y_blob2)
    dfx = dfx.compute()
    dfy = dfy.compute()
    dfx.to_csv(os.path.join('E:\InformationSystemsData', 'X_blob2.csv'))
    dfy.to_csv(os.path.join('E:\InformationSystemsData', 'y_blob2.csv'))
    del dfx
    del dfy
    del X_blob2
    del y_blob2

    X_class2, y_class2 = make_regression(n_samples=100000, n_features=1000, chunks=1000)
    dfx = dd.io.from_dask_array(X_class2)
    dfy = dd.io.from_dask_array(y_class2)
    dfx = dfx.compute()
    dfy = dfy.compute()
    dfx.to_csv(os.path.join('E:\InformationSystemsData', 'X_class2.csv'))
    dfy.to_csv(os.path.join('E:\InformationSystemsData', 'y_class2.csv'))
    del dfx
    del dfy
    del X_class2
    del y_class2

    X_reg3, y_reg3 = make_regression(n_samples=1000000, n_features=500, chunks=500)
    dfx = dd.io.from_dask_array(X_reg3)
    dfy = dd.io.from_dask_array(y_reg3)
    dfx = dfx.compute()
    dfy = dfy.compute()
    dfx.to_csv(os.path.join('E:\InformationSystemsData', 'X_reg3.csv'))
    dfy.to_csv(os.path.join('E:\InformationSystemsData', 'y_reg3.csv'))
    del dfx
    del dfy
    del X_reg3
    del y_reg3

    X_blob3, y_blob3 = make_regression(n_samples=1000000, n_features=500, chunks=500)
    dfx = dd.io.from_dask_array(X_blob3)
    dfy = dd.io.from_dask_array(y_blob3)
    dfx = dfx.compute()
    dfy = dfy.compute()
    dfx.to_csv(os.path.join('E:\InformationSystemsData', 'X_blob3.csv'))
    dfy.to_csv(os.path.join('E:\InformationSystemsData', 'y_blob3.csv'))
    del dfx
    del dfy
    del X_blob3
    del y_blob3

    X_class3, y_class3 = make_regression(n_samples=1000000, n_features=500, chunks=500)
    dfx = dd.io.from_dask_array(X_class3)
    dfy = dd.io.from_dask_array(y_class3)
    dfx = dfx.compute()
    dfy = dfy.compute()
    dfx.to_csv(os.path.join('E:\InformationSystemsData', 'X_class3.csv'))
    dfy.to_csv(os.path.join('E:\InformationSystemsData', 'y_class3.csv'))
    del dfx
    del dfy
    del X_class3
    del y_class3

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
