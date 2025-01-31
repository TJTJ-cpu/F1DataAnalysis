from urllib.request import urlopen
import pandas as pd
import json

from pandas.core.common import consensus_name_attr


def ExportToExcel(fileName, Data):
    Data.to_excel(f'{fileName}.xlsx', index=False)

def UrlToDataFrame(url):
    response = urlopen(url)
    dt = json.loads(response.read().decode('utf-8'))
    return pd.DataFrame(dt)

def FormatDate_DDMMYY(data, cName):
    data[cName] = pd.to_datetime(data[cName]).dt.strftime('%d-%m-%y')
    return data

def FormatTime_HHMMSS(data, cName):
    data[cName] = pd.to_datetime(data[cName]).dt.strftime('%H:%M:%S.%f').str[:-3]
    return data

def RemoveDulplicate(data, cName):
    return data.drop_duplicates(subset=[cName])

def RemoveRowIfZero(data, cName, val=0):
    # Remove the val that is 0
    data = data.drop(data[data[cName] == val].index)
    # Reset the index
    data = data[data[cName] != 0].reset_index(drop=True)
    return data


# Make a func that filter out a certain type
# def FilterOut(data, cName, cVal):

