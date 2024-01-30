import ray
from ray.train import ScalingConfig
from ray.train.xgboost import XGBoostTrainer
import sys


def distributed():
    sys.setrecursionlimit(100000)

    # Load data.
    dataset = ray.data.read_csv(r"E:\InformationSystemsData\data\reg2_full.csv", parallelism=8)

    # Split data into train and validation.
    train_dataset, valid_dataset = dataset.train_test_split(test_size=0.3)

    trainer = XGBoostTrainer(
        scaling_config=ScalingConfig(
            # Number of workers to use for data parallelism.
            num_workers=8,
            # Whether to use GPU acceleration. Set to True to schedule GPU workers.
            use_gpu=False,
        ),
        label_column="target",
        num_boost_round=20,
        params={
            # XGBoost specific params (see the `xgboost.train` API reference)
            "objective": "binary:logistic",
            # uncomment this and set `use_gpu=True` to use GPU for training
            # "tree_method": "gpu_hist",
            "eval_metric": ["logloss", "error"],
        },
        datasets={"train": train_dataset, "valid": valid_dataset},
        # If running in a multi-node cluster, this is where you
        # should configure the run's persistent storage that is accessible
        # across all worker nodes.
        # run_config=ray.train.RunConfig(storage_path="s3://..."),
    )
    result = trainer.fit()
    print(result.metrics)
