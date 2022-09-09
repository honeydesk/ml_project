import pandas as pd
import os
from housing.pipeline.pipeline import Pipeline

def get_experiments_status(experiment_file_path, limit: int = 5) -> pd.DataFrame:
    if os.path.exists(experiment_file_path):
        df = pd.read_csv(experiment_file_path)
        limit = -1 * int(limit)
        return df[limit:].drop(columns=["experiment_file_path", "initialization_timestamp"], axis=1)
    else:
        return pd.DataFrame()


Pipeline.experiment.experiment_file_path

experiment_file_path = '/home/honey/Desktop/Ineuron_ML_Project/ml_project/housing/artifact/experiment/experiment.csv'

print(get_experiments_status(experiment_file_path))
