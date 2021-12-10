from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
import os
import time

# create an engine to connect to the team54database database
engine = create_engine('mysql+pymysql://admin:PASSWORD@team54data.cz2kgult6cas.us-east-1.rds.amazonaws.com:3306/team54database')

# read data from CSV and load into a dataframe object
data = pd.read_csv('Bridge_Predictions.csv', encoding = "ISO-8859-1")

start_time = time.time()

try:
    # write data into the table
    data.to_sql('BRIDGE_CONDITION_MODEL_PREDICTIONS', engine, if_exists='append', chunksize=1000, method='multi', index=False)
except SQLAlchemyError as e:
    error = str(e.__dict__['orig'])
    print(error)
    exit()

print("--- %s seconds ---" % (time.time() - start_time))
print(" successfully loaded...")

# file_list = ["Cleaned_Full_Data.csv"]
# file_list = ["Cleaned_Full_Data_V_2.csv"]
# # file_list = os.listdir("InfoBridgeData/")

# for file in file_list:
    
#     # data = pd.read_csv("InfoBridgeData/" + file, encoding = "ISO-8859-1")
#     data = pd.read_csv(file, encoding = "ISO-8859-1")

#     # get data year from filename and add as new column
#     # data['DATA_YEAR'] = file[len(file)-8:len(file)-4]

#     print("Number of rows " + str(data.shape[0]) + ".")

#     # column_drop_list = ["CRITICAL_FACILITY_006B","HIGHWAY_DISTRICT_002","MIN_VERT_CLR_010","BASE_HWY_NETWORK_012","LRS_INV_ROUTE_013A","SUBROUTE_NO_013B","FUNCTIONAL_CLASS_026","APPR_WIDTH_MT_032","DEGREES_SKEW_034","STRUCTURE_FLARED_035","RAILINGS_036A","TRANSITIONS_036B","APPR_RAIL_036C","APPR_RAIL_END_036D","APPR_SPANS_046","HORR_CLR_MT_047","LEFT_CURB_MT_050A","RIGHT_CURB_MT_050B","ROADWAY_WIDTH_MT_051","DECK_WIDTH_MT_052","VERT_CLR_OVER_MT_053","VERT_CLR_UND_REF_054A","VERT_CLR_UND_054B","LAT_UND_REF_055A","LAT_UND_MT_055B","LEFT_LAT_UND_MT_056","OPR_RATING_METH_063","INV_RATING_METH_065","STRUCTURAL_EVAL_067","DECK_GEOMETRY_EVAL_068","UNDCLRENCE_EVAL_069","POSTING_EVAL_070","WATERWAY_EVAL_071","APPR_ROAD_EVAL_072","WORK_DONE_BY_075B","IMP_LEN_MT_076","FRACTURE_092A","UNDWATER_LOOK_SEE_092B","SPEC_INSPECT_092C","FRACTURE_LAST_DATE_093A","UNDWATER_LAST_DATE_093B","SPEC_LAST_DATE_093C","STRAHNET_HIGHWAY_100","PARALLEL_STRUCTURE_101","TEMP_STRUCTURE_103","SURFACE_TYPE_108A","MEMBRANE_TYPE_108B","DECK_PROTECTION_108C","NATIONAL_NETWORK_110","PIER_PROTECTION_111","BRIDGE_LEN_IND_112","SCOUR_CRITICAL_113","MIN_NAV_CLR_MT_116","FED_AGENCY","SUBMITTED_BY","LOWEST_RATING","CAT23","DATE_LAST_UPDATE","TYPE_LAST_UPDATE","DEDUCT_CODE","REMARKS","PROGRAM_CODE","PROJ_NO","PROJ_SUFFIX","NBI_TYPE_OF_IMP","DTL_TYPE_OF_IMP","SPECIAL_CODE","STEP_CODE","STATUS_WITH_10YR_RULE","SUFFICIENCY_ASTERC","SUFFICIENCY_RATING","STATUS_NO_10YR_RULE","STATUS"]
#     # data = data.drop(column_drop_list, axis=1, errors='ignore')

#     # data.rename(columns = {'CAT10':'BRIDGE_CONDITION', 'CAT29':'DECK_AREA'}, inplace=True)

#     # if 'DECK_AREA' not in data:
#     #     data['DECK_AREA'] = ""

#     # if 'BRIDGE_CONDITION' not in data:
#     #     data['BRIDGE_CONDITION'] = ""

#     # uncomment below line to get create_table script
#     # print(pd.io.sql.get_schema(data, 'DOT_FHA_LTBP_InfoBridge'))

#     # uncomment to get a list of the columns
#     # for col in data.columns:
#     #     print(col)
#     # print()

#     print("Beginning insert of " + str(file) + " into database...")

#     start_time = time.time()

#     try:
#         # write data into the table
#         data.to_sql('DOT_FHA_LTBP_InfoBridge', engine, if_exists='append', chunksize=1000, method='multi', index=False)
#     except SQLAlchemyError as e:
#         error = str(e.__dict__['orig'])
#         print(error)
#         exit()

#     print("--- %s seconds ---" % (time.time() - start_time))
#     print(str(file) + " successfully loaded...")