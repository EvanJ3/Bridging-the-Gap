import numpy as np
import pandas as pd
from column_conversion_dictionaries import *

def filter_sci_notation(df_input,col_name='STRUCTURE_NUMBER'):
    '''
    Filters and or converts scientific notation string entries in a given column
    into a correspoinding integer
    '''
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: format_sci_notation(x) if not(pd.isna(x)) else 'NaN')
    return df
    
def format_sci_notation(entry):
    '''
    Formats a string containing scientific notation to a string of integers
    '''
    if 'E+' in entry and '.' in entry:
        spilt_entry = entry.split('.')
        pre_decimal = spilt_entry[0]
        post_decimal = spilt_entry[1]
        sci_split = post_decimal.split('E+')
        front = sci_split[0]
        back = sci_split[1]
        back_int = int(back)
        back_int = back_int - len(front)
        back_pad = '0'*back_int
        return pre_decimal + front + back_pad
    elif 'E+' in entry:
        split_entry = entry.split('E+')
        front = split_entry[0]
        back = split_entry[1]
        back_pad = '0'*int(back)
        return front+back_pad
    else:
        return entry

    
def remove_duplicate_structs(df_input,struct_col_name='STRUCTURE_NUMBER_008',year_col_name='YEAR_BUILT_027'):
    '''
    Removes duplicate entries of structures with same state and strucutre code. First it identifies duplicates then it sorts
    all of the found duplicates by "year built" then keeps only the newest built structure removing the rest
    '''
    df = df_input.copy()
    df = df.sort_values([struct_col_name,year_col_name],ascending=False,axis=0)
    df = df.drop_duplicates(subset=[struct_col_name],keep='first')
    return df


def filter_ts_cols(df_input):
    '''
    Filters out all columns from the dataframe not inlcuded in ts_cols list above
    '''
    df = df_input.copy()
    df_col_list = list(df.columns)
    for i in df_col_list:
        if not(i in ts_cols):
            df.drop([i],axis=1,inplace=True)
        else:
            pass
    return df


def format_column_names(df_input,year_string):
    '''
    Removes column suffixes
    '''
    df = df_input.copy()
    df_col_list = list(df.columns)
    for i in range(0,len(df_col_list)):
        if df_col_list[i] in ['SUFFICIENCY_RATING','BRIDGE_CONDITION']:
            new_name = df_col_list[i]+'_'+year_string
            df.rename(columns={df_col_list[i]:new_name},inplace=True)
        else:
            stripped_name = df_col_list[i][:-4]
            new_name = stripped_name+'_'+year_string
            df.rename(columns={df_col_list[i]:new_name},inplace=True)
    return df


def clean_scour_critical_codes(df_input,col_name='SCOUR_CRITICAL_113'):
    '''
    Cleans the scour critical codes according to scour ciritical dict if not in dict set to NaN
    '''
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: clean_scour_entry(x) if not(pd.isna(x)) else 'NaN')
    return df

def clean_scour_entry(x):
    '''
    Helper function for clean scour cirtical codes serves as a catch for nan
    '''
    scour_acceptable_list = list(Scour_Critical_Dict.keys())
    if x in scour_acceptable_list:
        return x
    else:
        return 'NaN'
    
    
def remove_decimals_from_string_integers(df_input,col_name):
    '''
    Splits strings in float format and converts them to strings of integers
    '''
    df = df_input.copy()
    if col_name in list(df.columns):
        df[col_name] = df[col_name].apply(lambda x: string_integer_formatter(x) if not(pd.isna(x)) else 'NaN')
    return df

def string_integer_formatter(entry):
    '''
    Splits strings in float format and converts them to strings of integers
    '''
    if '.' in entry:
        return entry.split('.')[0]
    else:
        return entry

    
def get_integer_cols(df_input):
    '''
    Identifies all df columns that should take on only integer encodings 
    Serves as a preprocessing step before applying clean eval decimal cols
    '''
    df = df_input.copy()
    df_col_list = list(df.columns)
    df_col_list.remove('STATE_CODE_001')
    df_col_list.remove('STRUCTURE_NUMBER_008')
    df_col_list.remove('YEAR_BUILT_027')
    if 'SUFFICIENCY_RATING' in df_col_list:
        df_col_list.remove('SUFFICIENCY_RATING')
        
    if 'BRIDGE_CONDITION' in df_col_list:
        df_col_list.remove('BRIDGE_CONDITION')
    
    return df_col_list

def clean_eval_decimal_cols(df_input,eval_col_list):
    '''
    Cleans any decimals that are found in integer only encoded columns
    '''
    df = df_input.copy()
    for i in range(0,len(eval_col_list)):
        df = remove_decimals_from_string_integers(df,col_name=eval_col_list[i])
    return df


def get_eval_cols(df_input):
    '''
    Identifies all of the structural eval column names 
    helper function for clean eval codes
    '''
    df = df_input.copy()
    df_col_list = list(df.columns)
    df_col_list.remove('STATE_CODE_001')
    df_col_list.remove('STRUCTURE_NUMBER_008')
    df_col_list.remove('YEAR_BUILT_027')
    if 'SUFFICIENCY_RATING' in df_col_list:
        df_col_list.remove('SUFFICIENCY_RATING')
        
    if 'BRIDGE_CONDITION' in df_col_list:
        df_col_list.remove('BRIDGE_CONDITION')
        
    if 'SCOUR_CRITICAL_113' in df_col_list:
        df_col_list.remove('SCOUR_CRITICAL_113')
    
    return df_col_list


def clean_eval_codes(df_input,col_names_list):
    '''
    Cleans any ill formatted eval code entries
    '''
    
    df = df_input.copy()
    for i in range(0,len(col_names_list)):
        if col_names_list[i] in list(df.columns):
            df[col_names_list[i]] = df[col_names_list[i]].apply(lambda x: clean_eval_entry(x) if not(pd.isna(x)) else 'NaN')
    return df

def clean_eval_entry(x):
    '''
    Cleans any ill formatted eval code entries
    '''
    eval_acceptable_list = list(Structure_Appraisal_Rating_Dict.keys())
    if x in eval_acceptable_list:
        return x
    else:
        return 'NaN'
    
    
def combine_data_cols(df_input,year_list):
    '''
    Merges all eval ts columns into a single column for each evaluation type
    '''
    df_full = df_input.copy()
    #base_ts_col_names = ['DECK_COND','SUPERSTRUCTURE_COND']
    base_ts_col_names = ['DECK_COND','SUPERSTRUCTURE_COND','SUBSTRUCTURE_COND','CHANNEL_COND','CULVERT_COND','STRUCTURAL_EVAL','DECK_GEOMETRY_EVAL','WATERWAY_EVAL','APPR_ROAD_EVAL','SCOUR_CRITICAL']
    df_short = df_full[['STATE_CODE','STRUCTURE_NUMBER']]
    for i in range(0,len(base_ts_col_names)):
        base = base_ts_col_names[i]
        base_year_list = []
        for j in range(0,len(year_list)):
            base_year_list.append(base+'_'+year_list[j])
        base_cols_with_key = base_year_list
        base_cols_with_key.append('STATE_CODE')
        base_cols_with_key.append('STRUCTURE_NUMBER')
        df_sub_filter = df_full[base_cols_with_key]
        df_sub_filter[base+'_COMBINED'] = df_sub_filter[base_year_list].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
        new_col_string = base+'_COMBINED'
        df_sub_sub_filter = df_sub_filter[['STRUCTURE_NUMBER',new_col_string]]
        df_short = pd.merge(df_short, df_sub_sub_filter, left_on="STRUCTURE_NUMBER",right_on="STRUCTURE_NUMBER",how='left')
    return df_short

def combine_sufficency_cols(df_input,df_shorter,year_list):
    '''
    Merges all sufficency ts columns into a single column
    '''
    df_full = df_input.copy()
    #base_ts_col_names = ['DECK_COND','SUPERSTRUCTURE_COND']
    base_ts_col_names = ['SUFFICIENCY_RATING']
    df_short = df_shorter.copy()
    for i in range(0,len(base_ts_col_names)):
        base = base_ts_col_names[i]
        base_year_list = []
        for j in range(0,len(year_list)):
            base_year_list.append(base+'_'+year_list[j])
        base_cols_with_key = base_year_list
        base_cols_with_key.append('STATE_CODE')
        base_cols_with_key.append('STRUCTURE_NUMBER')
        df_sub_filter = df_full[base_cols_with_key]
        df_sub_filter[base+'_COMBINED'] = df_sub_filter[base_year_list].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
        new_col_string = base+'_COMBINED'
        df_sub_sub_filter = df_sub_filter[['STRUCTURE_NUMBER',new_col_string]]
        df_short = pd.merge(df_short, df_sub_sub_filter, left_on="STRUCTURE_NUMBER",right_on="STRUCTURE_NUMBER",how='left')
    return df_short