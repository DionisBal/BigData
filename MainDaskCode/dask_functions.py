import dask.dataframe as dd
from dask.distributed import Client

client = Client()


def parallel_sort(path, value=0):
    df = dd.read_csv(path)
    # df = df[df[value] < 0]
    # result = df.groupby(df.name).amount.mean()
    # result = result.compute()  # Compute to get pandas result
    # result.plot()
    return
