# We have used this function in 'data_transformation.py'

from housing.constant import *
from housing.util.util import read_yaml_file,save_object,save_numpy_array_data,load_data
import pandas as pd

file_path = r"/home/honey/Desktop/Ineuron_ML_Project/ml_project/housing/artifact/data_ingestion/2022-08-22-22-31-07/ingested_data/train/housing.csv"
schema_file_path = r"/home/honey/Desktop/Ineuron_ML_Project/ml_project/config/schema.yaml"

def load_data(file_path: str, schema_file_path: str) -> pd.DataFrame:
    try:
        datatset_schema = read_yaml_file(schema_file_path)

        schema = datatset_schema[DATASET_SCHEMA_COLUMNS_KEY]

        dataframe = pd.read_csv(file_path)

        error_messgae = ""


        for column in dataframe.columns:
            if column in list(schema.keys()):
                dataframe[column].astype(schema[column])
            else:
                error_messgae = f"{error_messgae} \nColumn: [{column}] is not in the schema."
        if len(error_messgae) > 0:
            raise Exception(error_messgae)
        return dataframe

    except Exception as e:
        raise HousingException(e,sys) from e

    
df = load_data(file_path=file_path,schema_file_path=schema_file_path)
print(df.columns)
print(df.dtypes)
