import numpy as np
import pandas as pd
from column_conversion_dictionaries import *


def format_structure_number(entry):
    entry = entry.lstrip('0')
    return entry

def remove_leading_zeros_strut(df_input,col_name='STRUCTURE_NUMBER'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: format_structure_number(x))
    return df

def county_code_formatter(state_code,code_float):
    state_code = int(state_code)
    integer_version = int(code_float)
    if integer_version >= 100:
        return str(state_code)+str(integer_version)
    elif integer_version >= 10:
        return str(state_code)+str(0)+str(integer_version)
    else:
        return str(state_code)+str(0)+str(0)+str(integer_version)

def state_code_converter(df_input,col_name='STATE_CODE'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: fips_state_code_dict.get(x.lstrip('0'),'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def county_code_converter(df_input,state_col_name='STATE_CODE',county_col_name='COUNTY_CODE'):
    df = df_input.copy()
    fips_state_code_dict_inv = dict((v,k) for k,v in fips_state_code_dict.items())
    df[county_col_name] = df.apply(lambda x: fips_to_county_dict.get(county_code_formatter(fips_state_code_dict_inv[x[state_col_name]],x[county_col_name]),'NaN'),axis=1)
    return df

def direction_code_converter(df_input,col_name='DIRECTION'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Direction_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def service_level_code_converter(df_input,col_name='SERVICE_LEVEL'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Service_Level_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def route_prefix_code_converter(df_input, col_name='ROUTE_PREFIX'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Route_Prefix_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def toll_code_converter(df_input,col_name='TOLL'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Toll_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def functional_classification_code_formatter(entry):
    if int(entry) >= 10:
        return str(int(entry))
    else:
        return str('0') + str(int(entry))

def functional_classification_code_converter(df_input,col_name='FUNCTIONAL_CLASS'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Functional_Classification_Dict[functional_classification_code_formatter(x)] if not(pd.isna(x))  else 'NaN')
    return df

def service_under_code_converter(df_input,col_name='SERVICE_UND'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Service_Under_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def service_over_code_converter(df_input,col_name='SERVICE_ON'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Service_On_Dict.get(x,'NaN') if not(pd.isna(x))  else 'NaN')
    return df

def open_close_status_code_converter(df_input,col_name='OPEN_CLOSED_POSTED'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Structure_Open_Closed_Posted_Dict.get(x,'NaN'))
    return df


def structure_kind_code_conversion(df_input,col_name='STRUCTURE_KIND'):
    '''Also used on cols APPR_KIND_044A'''
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Structure_Kind_Dict.get(x,'NaN') if not(pd.isna(x))  else 'NaN')
    return df

def structure_type_formatter(entry):
    if int(entry) >= 10:
        return str(int(entry))
    else:
        return str('0') + str(int(entry))

def structure_type_code_conversion(df_input,col_name='STRUCTURE_TYPE'):
    '''Also used on cols APPR_TYPE_044B'''
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Structure_Type_Dict[structure_type_formatter(x)] if not(pd.isna(x)) else 'NaN')
    return df

def type_of_work_code_conversion(df_input, col_name='WORK_PROPOSED'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Type_of_Work_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df


def deck_structure_code_conversion(df_input, col_name='DECK_STRUCTURE_TYPE'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Deck_Structure_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df


def surface_type_code_conversion(df_input,col_name='SURFACE_TYPE'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Surface_Type_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def membrane_type_code_conversion(df_input,col_name='MEMBRANE_TYPE'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Membrane_Type_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def deck_protection_code_conversion(df_input,col_name='DECK_PROTECTION'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Deck_Protection_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def bridge_condition_code_conversion(df_input,col_name='BRIDGE_CONDITION'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Bridge_Condition_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def pier_protection_code_conversion(df_input,col_name='PIER_PROTECTION'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Pier_Protection_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def traffic_direction_code_conversion(df_input,col_name='TRAFFIC_DIRECTION'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Traffic_Direction_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def condition_rating_code_conversion(df_input,col_name='DECK_COND'):
    '''Also used on cols  SUPERSTRUCTURE_COND_059 SUBSTRUCTURE_COND_060 CHANNEL_COND_061 CULVERT_COND_062'''
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Condition_Rating_Dict_Short.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def design_load_code_conversion(df_input, col_name='DESIGN_LOAD'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Design_Load_Metric_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def structure_appr_code_conversion(df_input,col_name='STRUCTURAL_EVAL'):
    '''Also used on cols DECK_GEOMETRY_EVAL_068 UNDCLRENCE_EVAL_069 POSTING_EVAL_070 WATERWAY_EVAL_071 APPR_ROAD_EVAL_072'''
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Structure_Appraisal_Rating_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def posting_eval_code_conversion(df_input,col_name='POSTING_EVAL'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Posting_Rating_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def work_done_by_code_conversion(df_input,col_name='WORK_DONE_BY'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Work_Done_By_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def operating_method_rating_code_conversion(df_input,col_name='OPR_RATING_METH'):
    '''Also used with INV_RATING_METH'''
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: Operating_Rating_Method_Dict.get(x,'NaN') if not(pd.isna(x)) else 'NaN')
    return df

def special_inpection_code_converter(df_input,col_name='SPEC_INSPECT'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: special_inspection_formatter(x) if not(pd.isna(x)) else 'NaN')
    return df

def special_inspection_formatter(x):
    if 'n' in x.lower():
        return 'NaN'
    else:
        return x[1:]+' Months'
    
def month_year_converter(df_input,col_name='DATE_OF_INSPECT'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: month_year_formatter(x) if not(pd.isna(x)) else 'NaN')
    return df

def month_year_formatter(x):
    try:
        x_int = int(x)
        
        if x_int >= 1000:
            return x[0:2]+'-'+'20'+x[2:]
        else:
            return '0'+x[0]+'-'+'20'+x[1:]
    except ValueError:
        return 'NaN'
    

def remove_decimals_from_string_integers(df_input,col_name):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: string_integer_formatter(x) if not(pd.isna(x)) else 'NaN')
    return df

def string_integer_formatter(entry):
    if '.' in entry:
        return entry.split('.')[0]
    else:
        return entry
 
    
def clean_scour_critical_codes(df_input,col_name='SCOUR_CRITICAL_113'):
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: clean_scour_entry(x) if not(pd.isna(x)) else 'NaN')
    return df

def clean_scour_entry(x):
    scour_acceptable_list = list(Scour_Critical_Dict.keys())
    if x in scour_acceptable_list:
        return x
    else:
        return 'NaN'
    
    
def clean_eval_codes(df_input,col_names_list=['DECK_COND_058','SUPERSTRUCTURE_COND_059','SUBSTRUCTURE_COND_060','CHANNEL_COND_061','CULVERT_COND_062','STRUCTURAL_EVAL_067','DECK_GEOMETRY_EVAL_068', 'WATERWAY_EVAL_071','APPR_ROAD_EVAL_072']):
    df = df_input.copy()
    for i in range(0,len(col_names_list)):
        if col_names_list[i] in list(df.columns):
            df[col_names_list[i]] = df[col_names_list[i]].apply(lambda x: clean_eval_entry(x) if not(pd.isna(x)) else 'NaN')
    return df

def clean_eval_entry(x):
    eval_acceptable_list = list(Structure_Appraisal_Rating_Dict.keys())
    if x in eval_acceptable_list:
        return x
    else:
        return 'NaN'
    
    
def filter_ts_cols(df_input):
    df = df_input.copy()
    df_col_list = list(df.columns)
    for i in df_col_list:
        if not(i in ts_cols):
            df.drop([i],axis=1,inplace=True)
        else:
            pass
    return df

def filter_unused_columns(df,remove_cols=unused_cols_list):
    df_col_list = list(df.columns)
    for i in unused_cols_list:
        if i in df_col_list:
            df.drop(i, axis=1,inplace=True)
        else:
            pass
    return df