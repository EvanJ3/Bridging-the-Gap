from sqlalchemy import create_engine
import pandas as pd
import pymysql

# create an engine to connect to the team54database database
# REPLACE USERNAME AND PASSWORD WITH CREDENTIALS
engine = create_engine('mysql+pymysql://USERNAME:PASSWORD@team54data.cz2kgult6cas.us-east-1.rds.amazonaws.com:3306/team54database')

# Read in csv generated from traffic_file_read_in.ipynb
traffic_df_all = pd.read_csv('../../../traffic_df_all.csv', index_col=0)
traffic_df_all = traffic_df_all.rename(columns = {column:column.upper() for column in list(traffic_df_all.columns)})

traffic_df_all.to_sql('TRAFFIC_STATE_MONTH', engine, if_exists='append', method='multi', index=False)



