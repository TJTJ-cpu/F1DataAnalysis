from ssl import ALERT_DESCRIPTION_INSUFFICIENT_SECURITY
import matplotlib.pyplot as plt
import pandas as pd
from enum import Enum

import ApiUtlis
import DataUtlis
import os
import math
import time
import random


#################### FullStackFunction ####################
# Category Type
class CCategory(Enum):
    CarData = "CarData"
    Laps = "Laps"
    RaceControl = "RaceControl"

def FullDataGatheringFunc():
    keys = ApiUtlis.GetAllSessionKeys()
    keysNum = len(keys)
    print(f'Race Count: {keysNum}')
    random.shuffle(keys)
    # temp
    # keys = []
    # netherland 2024
    # keys.append(9582)
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
        LoopFinalPositionData(raceName, key)
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

def RainvsDriver(fileName):
    lapsDf = DataUtlis.ReadLapsData(fileName)
    posData = DataUtlis.ReadFinalPosition(fileName)
    weatherData = DataUtlis.ReadWeatherData(fileName)

    temp = weatherData['air_temperature'].mean()
    # print(f'{fileName} - Temp: {temp}')
    # print(temp)

    winnerRow = posData[posData['position'] == 1]
    if winnerRow.empty:
        return None
    winnerNum = winnerRow['driver_number'].values[0]
    highestLap = lapsDf[lapsDf['driver_number'] == winnerNum]['lap_number'].max()

    lastLap = lapsDf.groupby('driver_number')['lap_number'].max()
    finsihedDriver = lastLap[lastLap == highestLap].index

    lapsDf = lapsDf[['lap_number', 'driver_number' ]]
    lapsDf = lapsDf.dropna()

    final = DataUtlis.MergeDataFrame(posData, lapsDf, 'driver_number')
    final['air_temperature'] = temp
    print(final)

    return final


def LapsTimevsPosition(fileName):
    lapsDf = DataUtlis.ReadLapsData(fileName)
    posData = DataUtlis.ReadFinalPosition(fileName)
    weatherData = DataUtlis.ReadWeatherData(fileName)

    # higest lap
    winnerRow = posData[posData['position'] == 1]
    if winnerRow.empty:
        return None
    winnerNum = winnerRow['driver_number'].values[0]
    highestLap = lapsDf[lapsDf['driver_number'] == winnerNum]['lap_number'].max()

    lastLap = lapsDf.groupby('driver_number')['lap_number'].max()
    finsihedDriver = lastLap[lastLap == highestLap].index

    lapsDf = lapsDf[['lap_duration', 'lap_number', 'driver_number' ]]
    lapsDf = lapsDf.dropna()

    # AVERAGE TEMPERATURE
    temp = weatherData['air_temperature'].mean()

    # GET AVG
    lapsDf = lapsDf.groupby('driver_number', as_index=False)['lap_duration'].mean()
    lapsDf.rename(columns={'lap_duration': 'avg_lap_duration'}, inplace=True)

    final = DataUtlis.MergeDataFrame(lapsDf, posData, 'driver_number')
    final = final[['position', 'driver_number', 'avg_lap_duration']]
    # loop through driver num and check if na
    final = DataUtlis.RemoveNanRows(final)
    final['track_name'] = fileName
    final = final[final['driver_number'].isin(finsihedDriver)]
    final['air_temperature'] = temp
    return final    



#################### Looping Function  ####################

def LoopWeatherData(raceName, key):
    folderName = 'Weather' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'WeatherData'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetWeatherData(key)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)

def LoopStintsData(driver, raceName, key):
    folderName = 'Stint' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetStintsData(key, driver)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)

def LoopSessionData(raceName, key):
    folderName = 'Sessions' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'SessionsData'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetSessionDataByKey(key)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)

def LoopRaceControlData(raceName, key):
    folderName = 'RaceControl' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'RaceControlData'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetRaceControlData(key)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)

def LoopPositionData(driver, raceName, key):
    folderName = 'Position' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetPositionData(key, driver)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)

def LoopFinalPositionData(raceName, key):
    folderName = 'Position' 
    subPath = os.path.join(raceName, folderName)
    fileName = 'FinalPosition'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetPosition(key)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)

def LoopPitData(driver, raceName, key):
    folderName = 'Pit' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetPitData(key, driver)
        # data = DataUtlis.RemoveRowIf(data, 'lap_number', 1)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)

def LoopMeetingData(raceName ,countryName, year):
    folderName = 'Meetings' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'Meetings'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetMeetingData(countryName, year)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)


def LoopLocation(driver, raceName, key):
    folderName = 'Location' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetLocationData(key, driver)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)

def LoopLapsData(driver, raceName, key):
    folderName = 'Laps' 
    subPath = os.path.join(raceName, folderName)
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetLapsData(key, driver)
        DataUtlis.ExportToExcel(fileName, data, raceName, folderName)

def LoopIntervalData(driver, raceName, key):
    subPath = os.path.join(raceName, 'Intervals')
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetIntervalData(key, driver)
        DataUtlis.ExportToExcel(fileName, data, raceName, 'Intervals')


def LoopDriverData(raceName, key):
    fileName = 'Drivers'
    path = os.path.join(raceName, fileName)
    path = os.path.join(path, 'DriversData')
    if not DataUtlis.CheckIfFileExist(path):
        driverData = ApiUtlis.GetDriverData(key)
        DataUtlis.ExportToExcel(fileName, driverData, raceName, fileName)

def LoopCarData(driver, folderName, key):
    subPath = os.path.join(folderName, 'CarData')
    fileName = f'Driver_{driver}'
    path = os.path.join(subPath, fileName)
    if not DataUtlis.CheckIfFileExist(path):
        data = ApiUtlis.GetCarData(key, driver)
        DataUtlis.ExportToExcel(fileName, data, folderName, 'CarData')

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
