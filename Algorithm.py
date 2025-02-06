from ssl import ALERT_DESCRIPTION_INSUFFICIENT_SECURITY
import matplotlib.pyplot as plt
import pandas as pd

import ApiUtlis
import DataUtlis
import os
import math
import time
import random



#################### FullStackFunction ####################

def FS_Lap_Pos():
    # dataList = [[pos1, dura1], [pos2, dura2]]
    dataList = [[]]
    position = []
    duraArr = []
    tempList = [[]]
    keys = ApiUtlis.GetAllSessionKey()
    keys = [7779, 7953]
    for key in keys:
        # Get Keys
        print(key)
        df = ApiUtlis.GetPosition(key)
        tempList = [[]]

        # Track Info
        tk = ApiUtlis.GetTrackData(key)
        tkName = tk[['circuit_short_name', 'country_name', 'year']]
        print(tkName)

        # Iter
        for index, row in df.iterrows():
            driverNum = int(row.iloc[0])
            position = int(row.iloc[1])
            dura = ApiUtlis.DriverLapDuration(key, driverNum)
            temp = [position, float(dura)]
            print(temp)
            tempList.append([position, dura])

    # Spread Sheet
    df = pd.DataFrame(tempList, columns=['Age', 'Weight'])
    rVal = df['Age'].corr(df['Weight'])
    print(f'final rval: {rVal}')

    # print(dataList)
    # r val
    # plot 
    # df.plot.scatter(x='position', y='duration')
    # plt.show()

def FullDataGatheringFunc():
    keys = ApiUtlis.GetAllSessionKey()
    keysNum = len(keys)
    print(f'Race Count: {keysNum}')
    random.shuffle(keys)
    for i, key in enumerate(keys):
        # Create the file if it doesn't exist
        trackData = ApiUtlis.GetTrackData(key)
        trackData = trackData[['circuit_short_name', 'country_name', 'year']]
        countryName = trackData['country_name'][0]
        year = trackData['year'][0]
        raceName = f'{countryName}_{year}'
        DataUtlis.CreateSubFolder(raceName)

        print()
        print(f'{i + 1}: {countryName}-{year}')
        driverArr = ApiUtlis.GetALlDriverNumber(key)

        # Call One
        LoopWeatherData(raceName, key)
        LoopDriverData(raceName, key)
        LoopRaceControlData(raceName, key)
        LoopSessionData(raceName, key)
        # LoopMeetingData(raceName, countryName, year)
        for driver in driverArr:
            LoopStintsData(driver, raceName, key)
            LoopCarData(driver, raceName, key)
            LoopIntervalData(driver, raceName, key)
            LoopLapsData(driver, raceName, key)
            LoopPitData(driver, raceName, key)
            LoopPositionData(driver, raceName, key)

        # Drivers
    return

#################### Looping Function  ####################

def LoopWeatherData(raceName, key):
    folderName = 'Weather' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'WeatherData'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetWeatherData(key)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)
    else:
        print(f'{path} is already exists')

def LoopStintsData(driver, raceName, key):
    folderName = 'Stint' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetStintsData(key, driver)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)
    else:
        print(f'{path} is already exists')

def LoopSessionData(raceName, key):
    folderName = 'Sessions' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'SessionsData'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetSessionDataByKey(key)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)
    else:
        print(f'{path} is already exists')

def LoopRaceControlData(raceName, key):
    folderName = 'RaceControl' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'RaceControlData'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetRaceControlData(key)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)
    else:
        print(f'{path} is already exists')

def LoopPositionData(driver, raceName, key):
    folderName = 'Position' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetPositionData(key, driver)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)
    else:
        print(f'{path} is already exists')

def LoopPitData(driver, raceName, key):
    folderName = 'Pit' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetPitData(key, driver)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)
    else:
        print(f'{path} is already exists')

def LoopMeetingData(raceName ,countryName, year):
    folderName = 'Meetings' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'Meetings'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetMeetingData(countryName, year)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)
    else:
        print(f'{path} is already exists')


def LoopLocation(driver, raceName, key):
    folderName = 'Location' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetLocationData(key, driver)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)
    else:
        print(f'{path} is already exists')

def LoopLapsData(driver, raceName, key):
    folderName = 'Laps' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetLapsData(key, driver)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)
    else:
        print(f'{path} is already exists')

def LoopIntervalData(driver, raceName, key):
    subPath = os.path.join(raceName, 'Intervals')
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetIntervalData(key, driver)
        DataUtlis.ExportToExcel(fileName, data, raceName, 'Intervals')
    else:
        print(f'{path} is already exists')


def LoopDriverData(raceName, key):
    fileName = 'Drivers'
    path = os.path.join(raceName, fileName)
    path = os.path.join(path, 'DriversData')
    if not DataUtlis.CheckIfFileExist(path):
        driverData = ApiUtlis.GetDriverData(key)
        DataUtlis.ExportToExcel(fileName, driverData, raceName, fileName)
    else:
        print(f'{path} is already exists')

def LoopCarData(driver, folderName, key):
    subPath = os.path.join(folderName, 'CarData')
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetCarData(key, driver)
        DataUtlis.ExportToExcel(fileName, data, folderName, 'CarData')
    else:
        print(f'{path} is already exists')

#################### Algorithm  ####################
def PearsonCorrelation(dt, val1, val2):
    meanX = dt[val1].mean()
    meanY = dt[val2].mean()
    sumNumer = 0
    sumDenor1 = 0
    sumDenor2 = 0
    for index, row in dt.iterrows():
        xi = row.iloc[0]
        yi = row.iloc[1]
        numer = (xi - meanX)*(yi - meanY)
        denor1 = math.pow((xi - meanX),2)
        denor2 = math.pow((yi - meanY),2)
        sumNumer += numer
        sumDenor1 += denor1
        sumDenor2 += denor2
    denor = math.sqrt(sumDenor1 * sumDenor2)
    if denor == 0:
        return 0
    return sumNumer / denor

#############################################################
