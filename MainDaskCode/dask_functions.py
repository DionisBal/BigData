import dask.dataframe as dd
from dask_ml.model_selection import train_test_split


def parallel_read(path):
    df = dd.read_csv(path)
    pandas_df = df.compute()
    return df, pandas_df


def parallel_write(df, path):
    return


def parallel_train_test_split(df_x, df_y):
    x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, random_state=42, test_size=0.3)
    return x_train, x_test, y_train, y_test
