from DataUtlis import *
import DataUtlis
import random
import numpy as np
    

#################### Getting Data From API ####################

def GetCarData(sessionKey, driverNum):
    url = f'https://api.openf1.org/v1/car_data?driver_number={driverNum}&session_key={sessionKey}'
    return UrlToDataFrame(url)

def GetDriverData(sessionKey, driverNum):
    url = f'https://api.openf1.org/v1/drivers?driver_number={driverNum}&session_key={sessionKey}'
    return UrlToDataFrame(url)

def GetIntervalData(sessionKey, driverNum):
    url = f'https://api.openf1.org/v1/intervals?session_key={sessionKey}&driver_number={driverNum}'
    return UrlToDataFrame(url)

def GetLapsData(driverNum, sessionKey, lapNum = None):
    if lapNum is not None and lapNum > 1:
        url = f'https://api.openf1.org/v1/laps?session_key={sessionKey}&driver_number={driverNum}&lap_number={lapNum}'
    else:
        url = f'https://api.openf1.org/v1/laps?session_key={sessionKey}&driver_number={driverNum}'
    return UrlToDataFrame(url)

def GetLocationData(sessionKey, driverNum):
    url = f'https://api.openf1.org/v1/location?session_key={sessionKey}&driver_number={driverNum}'
    return UrlToDataFrame(url)

def GetMeetingData(year):
    url = f'https://api.openf1.org/v1/meetings?year={year}'
    return UrlToDataFrame(url)

def GetPitData(sessionKey, driverNum = None):
    if driverNum is None:
        url = f'https://api.openf1.org/v1/pit?session_key={sessionKey}'
    else:
        url = f'https://api.openf1.org/v1/pit?session_key={sessionKey}&driver_number={driverNum}'
    return UrlToDataFrame(url)

def GetPositionData(sessionKey, driverNum = None):
    if driverNum is None:
        url = f'https://api.openf1.org/v1/position?session_key={sessionKey}'
    else:
        url = f'https://api.openf1.org/v1/position?session_key={sessionKey}&driver_number={driverNum}'
    return UrlToDataFrame(url)

# Probably need more parameter for this one
def GetRaceControlData(sessionKey):
    url = f'https://api.openf1.org/v1/race_control?session_key={sessionKey}'
    return UrlToDataFrame(url)

def GetSessionData(year, sesType = None):
    if sesType is None:
        url = f'https://api.openf1.org/v1/sessions?year={year}'
    else:
        url = f'https://api.openf1.org/v1/sessions?year={year}&session_type={sesType}'
    return UrlToDataFrame(url)

def GetSprintData(sessionKey, driverNum = None):
    if driverNum is None:
        url = f'https://api.openf1.org/v1/sessions?session_key={sessionKey}'
    else:
        url = f'https://api.openf1.org/v1/sessions?session_key={sessionKey}&driver_number={driverNum}'
    return UrlToDataFrame(url)

def GetWeatherData(sessionKey):
    url = f'https://api.openf1.org/v1/weather?session_key={sessionKey}'
    return DataUtlis.FormatTime_HHMMSS(UrlToDataFrame(url), 'date')

def GetTeamRadioData(sessionKey, driverNum = None):
    if driverNum is None:
        url = f'https://api.openf1.org/v1/team_radio?session_key={sessionKey}'
    else:
        url = f'https://api.openf1.org/v1/team_radio?session_key={sessionKey}&driver_number={driverNum}'
    return UrlToDataFrame(url)

#################### Costumized Function ####################

def GetTrackData(sessionKey):
    url = f'https://api.openf1.org/v1/sessions?session_key={sessionKey}'
    dt = UrlToDataFrame(url)
    dt = dt[['date_start', 'country_name', 'circuit_short_name', 'year']]
    return DataUtlis.FormatDate_DDMMYY(dt, 'date_start')

def RandomSessionKey():
    year = [2024, 2023]
    dt = GetSessionData(random.choice(year), 'Race')
    return random.choice(dt['session_key'].to_numpy())

def GetAllSessionKey():
    keys = []
    temp = []
    dt1 = GetSessionData(2023, 'Race')
    # keys.append(dt['session_key'].to_numpy)
    dt2 = GetSessionData(2024, 'Race')
    # keys.append(dt['session_key'].to_numpy)
    dt = dt1._append(dt2, ignore_index=True)
    temp.append(dt['session_key'].values.tolist())
    for key in temp[0]:
        keys.append(key)
    return keys


