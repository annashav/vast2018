"""
Data cleaning script
"""

import pandas as pd
import re

FILE_PATH = 'AllBirds_Hour.csv'
OUTPUT_PATH = 'AllBirds_Hour_rename.csv'


def reformat_dates(dataframe): #month/day/year #year/month/day
    for index in dataframe.index:
        date = dataframe.at[index, "Date"]
        
        if(re.match("[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}", date)):
            date = date.split(sep="/")
            year = date[2]
            month = date[0]
            day = date[1]
            date[0] = year
            date[1] = month
            date[2] = day
            #Move the month to the center 
            dataframe.at[index, "Date"] = "-".join(date)

def am_pm_column(dataframe):
    am_pm = []
    for index in dataframe.index:
        time = dataframe.at[index, "Time"]
        if(re.match("[0-9]{1,2}:[0-9]{1,2}", time)):
            hour = int(time.split(":")[0])
            if(hour < 12):
                am_pm.append("am")
            else:
                am_pm.append("pm")
        else:
            am_pm.append(time)
    ampm_series = pd.Series(am_pm, index=dataframe.index)
    return ampm_series

def replace_missing(dataframe):
    for index in dataframe.index:
        time = dataframe.at[index, "Time"]
        if(re.match("[0-9]{1,2}:[0-9]{1,2}", time) == None):
            dataframe.at[index, "Time"] = "?"

def split_date(dataframe):
    year  = []
    month = []
    day   = []
    for index in dataframe.index:
        date = dataframe.at[index, "Date"].split('-')
        year.append(date[0])
        month.append(date[1])
        day.append(date[2])
    year = pd.Series(year, index=dataframe.index)
    month = pd.Series(month, index=dataframe.index)
    day = pd.Series(day, index=dataframe.index)
    
    dataframe["Year"]  = year
    dataframe["Month"] = month
    dataframe["Day"]   = day

def time_to_hour(dataframe):
    hours = []
    for index in dataframe.index:
        hour = dataframe.at[index, "Time"].split(":")[0]
        hours.append(hour)
    hours = pd.Series(hours, index=dataframe.index)
    dataframe["Hour"] = hours

def rename(dataframe):
    names = []
    for index in dataframe.index:
        name = dataframe.at[index, "English_name"][0:3].upper()
        names.append(name)
    names = pd.Series(names, index=dataframe.index)
    dataframe["English_name"] = names
        

dataframe = pd.read_csv(FILE_PATH)
dataframe.set_index('File_ID', inplace=True)
rename(dataframe)
dataframe.to_csv(OUTPUT_PATH)
#ampm = am_pm_column(dataframe)
#dataframe["AM_PM"] = ampm
#dataframe = dataframe[['English_name', 'Vocalization_type', 'Quality', 'Time', 'AM_PM', 'Date', 'X', 'Y']]
#dataframe = dataframe[['English_name', 'Vocalization_type', 'Quality', 'Hour', 'AM_PM',
#                       'Year', 'Month', 'Day', 'X', 'Y']]
dataframe.to_csv(OUTPUT_PATH)
