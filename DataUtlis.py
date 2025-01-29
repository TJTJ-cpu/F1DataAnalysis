from urllib.request import urlopen
import pandas as pd
import json


def ExportToExcel(fileName, Data):
    Data.to_excel(f'{fileName}.xlsx', index=False)


def GetCarData2(dNum, sessKey):
    url = f'https://api.openf1.org/v1/car_data?driver_number={dNum}&session_key={sessKey}&speed>=315'

    dt = UrlToDataFrame(url)
    dt = ConvertTimeToSecond(dt, 'date')
    return dt


def UrlToDataFrame(url):
    response = urlopen(url)
    dt = json.loads(response.read().decode('utf-8'))
    Data  = pd.DataFrame(dt)
    return Data

def GetAllSessionCode(year):
    sessionBaseUrl = 'https://api.openf1.org/v1/sessions?session_name=Race'
    sessionUrl = f'{sessionBaseUrl}&year={year}'

    sessionData = UrlToDataFrame(sessionUrl)
    # Change the date format
    sessionData['date_start'] = pd.to_datetime(sessionData['date_start']).dt.strftime('%d-%m-%Y')
    # print(sessionData.columns)
    return sessionData[['session_key', 'country_name', 'circuit_short_name', 'date_start']]

def GetPosition(sKey, dNum):
    baseUrl = 'https://api.openf1.org/v1/position?'
    sessionkey = f'session_key={sKey}'
    driverNum = f'driver_number={dNum}'

    url = f'{baseUrl}{sessionkey}&{driverNum}'
    dt = UrlToDataFrame(url)
    # print(dt.columns)
    dt['date'] = pd.to_datetime(dt['date']).dt.strftime('%d-%m-%y')
    Data  = pd.DataFrame(dt)
    return Data

def ConverTimeToddmmyyyy(data, cName):
    data[cName] = pd.to_datetime(data[cName]).dt.strftime('%d-%m-%y')
    return data

def ConvertTimeToSecond(data, cName):
    data[cName] = pd.to_datetime(data[cName]).dt.strftime('%H:%M:%S.%f').str[:-3]
    return data

def RemoveDulplicate(data, cName):
    return data.drop_duplicates(subset=[cName])

# Make a func that filter out a certain type
# def FilterOut(data, cName, cVal):

