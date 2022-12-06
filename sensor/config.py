import pymongo
import pandas as pd
import json
from dataclasses import dataclass
# Provide the mongodb localhost url to connect python to mongodb.
import os
@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_access_secret_key:str = os.getenv("AWS_SECRET_ACCESS_KEY")


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "class"
# mongo_client = pymongo.MongoClient('mongodb://localhost:27017/neurolabDB')

# mydatabase = mongo_client.APS
# # print(mydatabase)

# mycollection = mydatabase.SENSOR
# print(mycollection)
# cursor = mycollection.find()
# print(cursor)
# list_cur = list(cursor)
# print(list_cur)
# df = DataFrame(list_cur)
# print('Type of df:',type(df))

# print(mongo_client)
# df = pd.DataFrame(list(mongo_client['APS']['SENSOR'].find()))
# print(df)
