from os.path import isfile
from urllib.request import HTTPError, urlopen
from urllib.error import HTTPError
from warnings import catch_warnings
from matplotlib.colors import cnames
import pandas as pd
import matplotlib.pyplot as plt

import ApiUtlis
import Algorithm
import time
import json
import os
import random




#################### Excel Data Manupulation  ####################

def ReadFinalPosition(fileName):
    root = 'Data'
    cat = 'Position'
    path = os.path.join(root, fileName, cat, 'FinalPosition.xlsx')
    return pd.read_excel(path)

def ReadWeatherData(fileName):
    root = 'Data'
    cat = 'Weather'
    oriPath = os.path.join(root, fileName, cat)
    arr = ShowAllFile(oriPath)

    df = pd.DataFrame()
    path = os.path.join(oriPath, f'WeatherData.xlsx')
    df = pd.read_excel(path)
    return df

def ReadLapsData(fileName, driverNum = None):
    root = 'Data'
    cat = 'Laps'
    oriPath = os.path.join(root, fileName, cat)
    arr = ShowAllFile(oriPath)

    df = pd.DataFrame()
    if driverNum:
        path = os.path.join(oriPath, f'Driver_{driverNum}.xlsx')
        df = pd.read_excel(path)
    else:
        for driver in arr:
            path = os.path.join(oriPath, driver)
            df1 = pd.read_excel(path)
            df = df._append(df1, ignore_index= True)
    return df

def ReadCarData(fileName, driverNum = None):
    # handle drivernum
    root = 'Data'
    cat = 'CarData'
    oriPath = os.path.join(root, fileName, cat)
    arr = ShowAllFile(oriPath)

    df = pd.DataFrame()
    if driverNum:
        path = os.path.join(oriPath, f'Driver_{driverNum}.xlsx')
        df = pd.read_excel(path)
    else:
        for driver in arr:
            path = os.path.join(oriPath, driver)
            df1 = pd.read_excel(path)
            df = df._append(df1, ignore_index= True)
    return df

def ReadPitData(fileName, driverNum = None):
    # handle drivernum
    root = 'Data'
    cat = 'Pit'
    oriPath = os.path.join(root, fileName, cat)
    arr = ShowAllFile(oriPath)

    df = pd.DataFrame()
    if driverNum:
        path = os.path.join(oriPath, f'Driver_{driverNum}.xlsx')
        df = pd.read_excel(path)
    else:
        for driver in arr:
            path = os.path.join(oriPath, driver)
            df1 = pd.read_excel(path)
            df = df._append(df1, ignore_index= True)
    return df

def ReadFunc(path):
    return pd.read_excel(path)

def ShowAllFile(path):
    return os.listdir(path)

#################### Data Manipulating  ####################
    
def GetAllFolderNames():
    dir_path = os.path.join(os.getcwd(), "Data")
    return [f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))]

def MergeDataFrame(dt1, dt2, cName):
    return pd.merge(dt1, dt2, on=cName,how='right')

def AddNewColumn(data, val, cName ):
    data[cName] = val
    return data

def ResetIndex(data):
    return data.reset_index(drop=True)

def MoveColumn(data, index, cName):
    column = data.pop(cName)
    data.insert(index, cName ,column)
    return data

def SetIndex(data, cName):
    dt = data.set_index(cName, inplace=True)
    return dt

def ColumnToArray(dt, cName):
    foo = dt[cName].to_numpy()
    return foo

def RemoveRowIf(dt, column, val):
    return dt[dt[column] != val]

def RemoveNanRows(final):
    final = final.dropna(subset=['avg_lap_duration'])  # Drop rows where avg_lap_duration is NaN
    return final


# NEED TO RESTRUCTURE THE FUNC 
# def GetAddColumnApi(sessionKey, cName):


#################### Exporting Tools  ####################

def CreateSubFolder(fileName):
    rootFolder = 'Data'
    os.makedirs(rootFolder, exist_ok=True)
    subMain = os.path.join(rootFolder, fileName)
    os.makedirs(subMain, exist_ok=True)

def ExportToExcel(fileName, Data, folder, subFolder=None):
    rootFolder = 'Data'
    os.makedirs(rootFolder, exist_ok=True)
    subMain = os.path.join(rootFolder, folder)
    os.makedirs(subMain, exist_ok=True)
    rootFolder = subMain
    if subFolder:
        folderPath = os.path.join(rootFolder, subFolder)
        os.makedirs(folderPath, exist_ok=True)
        filePath = os.path.join(folderPath,f'{fileName}.xlsx')
    else:
        filePath = os.path.join(rootFolder, f'{fileName}.xlsx')
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

def CheckIfFileExist(path):
    root = 'Data'
    os.makedirs(root, exist_ok=True)
    path = f'{path}.xlsx'
    path = os.path.join(root, path)
    if os.path.isfile(path):
        return True 
    else:
        return False

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
            elif e.code == 500: 
                return None
            else:
                raise
    raise Exception("Exceeded maximum retries due to rate limiting")

#################### Data Visualization ####################

def ScatterPlot(df, val1, val2):
    df.plot.scatter(x=val1, y=val2)

def DisplayGraph(arr, cName):
    plt.figure(figsize=(10,6))
    for idx, df in enumerate(arr):  
        # plt.plot(df['position'], df['avg_lap_duration'], label=f'Dataset {idx+1}')
        plt.scatter(df['position'], df['avg_lap_duration'], label=f"Dataset {idx+1}")
    plt.xlabel("Position")
    plt.ylabel("Average Lap Duration")
    plt.title(f"{cName}")
    plt.legend()  # Show legend with dataset names
    plt.grid(True)
    plt.show()

def DisplayLineGraph(cDict, cName):
    correlations = list(cDict.values())
    folders = list(cDict.keys())

    colors = ['red' if c < 0 else 'blue' for c in correlations]

    plt.figure(figsize=(9, 9))
    plt.bar(folders, correlations, color=colors)
    plt.axhline(0, color='black', linewidth=1)  

    plt.xlabel("Race Events")
    plt.ylabel("Correlation (-1 to 1)")
    plt.title(cName)
    plt.xticks(rotation=45, ha='right')
    plt.ylim(-0.5, 1)  

    plt.show()


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

def RemoveRowIfNan(data, cName):
    # Remove the val that is 0
    data = data.drop(data[data[cName] == None].index)
    # Reset the index
    data = data[data[cName] != 0].reset_index(drop=True)
    return data


# Make a func that filter out a certain type
# def FilterOut(data, cName, cVal):

