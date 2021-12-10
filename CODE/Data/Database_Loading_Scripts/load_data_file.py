from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
import os
import time

# create an engine to connect to the team54database database
engine = create_engine('mysql+pymysql://admin:PASSWORD@team54data.cz2kgult6cas.us-east-1.rds.amazonaws.com:3306/team54database')

file = "MODEL_PREDICTIONS_V2.csv"

data = pd.read_csv(file, encoding = "ISO-8859-1")

print("Number of rows " + str(data.shape[0]) + ".")
print("Beginning insert of " + str(file) + " into database...")

start_time = time.time()

try:
    # write data into the table
    data.to_sql('BRIDGE_CONDITION_MODEL_PREDICTIONS', engine, if_exists='append', chunksize=1000, method='multi', index=False)
except SQLAlchemyError as e:
    error = str(e.__dict__['orig'])
    print(error)
    exit()

print("--- %s seconds ---" % (time.time() - start_time))
print(str(file) + " successfully loaded...")