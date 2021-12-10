from sqlalchemy import create_engine
import pandas as pd
import os
import time

# create an engine to connect to the team54database database
engine = create_engine('mysql+pymysql://admin:PASSWORDGOESHERE@team54data.cz2kgult6cas.us-east-1.rds.amazonaws.com:3306/team54database')

base_dir = "../../../Monthly_Weather/"
base_dir_loaded = "../../../Monthly_Weather/loaded/"
base_dir_error = "../../../Monthly_Weather/errored/"

file_list = os.listdir(base_dir)
file_list.remove(".DS_Store")
file_list.remove("loaded")
file_list.remove("errored")

file_num = len(file_list)
file_count = 0

for file in file_list:

    print("File name: " + str(file))
    
    data = pd.read_csv(base_dir+file, encoding = "ISO-8859-1")
    # data = pd.read_csv('/Users/jacobshalkhauser/Documents/GeorgiaTech/DVA/gsom_sample_csv.csv', encoding = "ISO-8859-1")
    
    data['DATE'] = pd.to_datetime(data['DATE']) # convert the date column to a year type
    data = data[data['DATE'].dt.year >= 1990] # filter to years greater than (or equal to) 1990

    # print("Number of rows " + str(data.shape[0]) + ".")

    column_drop_list = ["DP1X","DP1X_ATTRIBUTES","DYFG","DYFG_ATTRIBUTES","DYTS","DYTS_ATTRIBUTES","EVAP","EVAP_ATTRIBUTES","TAVG","TAVG_ATTRIBUTES","WDMV","WDMV_ATTRIBUTES","WDMV_ATTRIBUTES","DYFG","DYFG_ATTRIBUTES","DYTS","DYTS_ATTRIBUTES","CLDD_ATTRIBUTES","HTDD_ATTRIBUTES","DX32","DX32_ATTRIBUTES","DX70","DX70_ATTRIBUTES","DX90","DX90_ATTRIBUTES","DT00","DT00_ATTRIBUTES","DT32","DT32_ATTRIBUTES","DP01","DP01_ATTRIBUTES","DP05","DP05_ATTRIBUTES","DP10","DP1X","DP1X_ATTRIBUTES","DP10_ATTRIBUTES","EMXP_ATTRIBUTES","EMSD_ATTRIBUTES","EMSN_ATTRIBUTES","DSND_ATTRIBUTES","DSNW_ATTRIBUTES","PRCP_ATTRIBUTES","SNOW_ATTRIBUTES","CDSD","CDSD_ATTRIBUTES","EMXT_ATTRIBUTES","EMNT_ATTRIBUTES","HDSD","HDSD_ATTRIBUTES","TMAX_ATTRIBUTES","TMIN_ATTRIBUTES","AWND_ATTRIBUTES","WDF2","WDF2_ATTRIBUTES","WDF5","WDF5_ATTRIBUTES","WSF2","WSF2_ATTRIBUTES","WSF5","WSF5_ATTRIBUTES"]
    data = data.drop(column_drop_list, axis=1, errors='ignore')

    # data.rename(columns = {'CAT10':'BRIDGE_CONDITION', 'CAT29':'DECK_AREA'}, inplace=True)

    # if 'DECK_AREA' not in data:
    #     data['DECK_AREA'] = ""

    # if 'BRIDGE_CONDITION' not in data:
    #     data['BRIDGE_CONDITION'] = ""

    # uncomment below line to get create_table script
    # print(pd.io.sql.get_schema(data, 'NOAA_NCDC_US_WTHR_MONTHLY'))

    # uncomment to get a list of the columns
    # for col in data.columns:
    #     print(col)
    # print()

    print("Beginning insert of " + str(file) + " into database...")

    start_time = time.time()

    try:
        # write data into the table
        data.to_sql('NOAA_NCDC_US_WTHR_MONTHLY', engine, if_exists='append', method='multi', index=False)
    except Exception:
        print("An exception occurred")
        os.rename(base_dir+file, base_dir_error+file) # move the file to the loaded directory
        continue

    os.rename(base_dir+file, base_dir_loaded+file) # move the file to the loaded directory

    file_count+=1
    print("--- %s seconds ---" % (time.time() - start_time))
    print(str(file) + " successfully loaded... " + str(file_count) + " of " + str(file_num))

