from DataUtlis import *
import DataUtlis
    

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
    return DataUtlis.ConvertTimeToSecond(UrlToDataFrame(url), 'date')

def GetTeamRadioData(sessionKey, driverNum = None):
    if driverNum is None:
        url = f'https://api.openf1.org/v1/team_radio?session_key={sessionKey}'
    else:
        url = f'https://api.openf1.org/v1/team_radio?session_key={sessionKey}&driver_number={driverNum}'
    return UrlToDataFrame(url)



