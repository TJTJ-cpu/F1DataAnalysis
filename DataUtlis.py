from urllib.request import HTTPError, urlopen
from urllib.error import HTTPError
import pandas as pd
from pandas.core.common import consensus_name_attr
import ApiUtlis
import time
import json
import os



#################### Exporting Tools  ####################

def ExportToExcel(fileName, Data, SubFolder=None):
    if SubFolder:
        os.makedirs(SubFolder, exist_ok=True)
        filePath = os.path.join(SubFolder,f'{fileName}.xlsx')
    else:
        filePath = f'{fileName}.xlsx'
    try:
        Data.to_excel(filePath, index=False)
        print(f'Exported "{filePath}" seccessfully!')
    except Exception as e:
          print("Error exporting file:", e)

def ExportPositionData(dt, key):
    # Track Data
    tk = ApiUtlis.GetTrackData(key)
    year = str(tk['year'][0])
    circuitName = str(tk['circuit_short_name'][0])
    # Export to Excel
    fileName = f'{circuitName}_{year}_PosData'
    dtSorted = dt.sort_values('date')
    final = dtSorted.groupby('driver_number').last().reset_index()
    final = final.sort_values('position')
    ExportToExcel(fileName, final, 'Data')

#################### Data Manipulating  ####################
    
def MergeDataFrame(dt1, dt2, cName):
    return pd.merge(dt1, dt2, on=cName,how='right')

#################### ExportingTools  ####################

def UrlToDataFrame(url, retries=5, waitFactor=2):
    for attemp in range(retries):
        try:
            response = urlopen(url)
            dt = json.loads(response.read().decode('utf-8'))
            return pd.DataFrame(dt)
        except HTTPError as e:
            if e.code == 429:
                retryAfter = e.headers.get('Retry-After')
                if retryAfter:
                    wait = int (retryAfter)
                else:
                    wait = waitFactor ** attemp
                time.sleep(wait)
            else:
                raise
    raise Exception("Exceeded maximum retries due to rate limiting")

#################### Date Formatting ####################

def FormatDate_DDMMYY(data, cName):
    data[cName] = pd.to_datetime(data[cName]).dt.strftime('%d-%m-%y')
    return data

def FormatTime_HHMMSS(data, cName):
    data[cName] = pd.to_datetime(data[cName], errors='coerce')
    data[cName] = data[cName].dt.strftime('%H:%M:%S.%f').str[:-3]
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

