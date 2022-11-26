# Dump aps.csv data to mongo DB 

import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")


DATA_FILE_PATH = '/config/workspace/aps_failure_training_set1.csv'
DATABASES_NAME = 'APS'
COLLECTION_NAME = 'SENSOR'

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(df.head())
    
    # Convert DF to JSON, so that we can dump these to mongoDB
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())  # .T convert rows and cols
    print(json_record[0])

    client[DATABASES_NAME][COLLECTION_NAME].insert_many(json_record)