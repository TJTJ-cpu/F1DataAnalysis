from DataUtlis import *
import DataUtlis
import random
import numpy as np
    

#################### Getting Data From API ####################

def GetCarData(sessionKey, driverNum):
    url = f'https://api.openf1.org/v1/car_data?driver_number={driverNum}&session_key={sessionKey}'
    return UrlToDataFrame(url)

def GetDriverData(sessionKey, driverNum=None):
    if driverNum:
        url = f'https://api.openf1.org/v1/drivers?driver_number={driverNum}&session_key={sessionKey}'
    else:
        url = f'https://api.openf1.org/v1/drivers?session_key={sessionKey}'
    return UrlToDataFrame(url)

def GetALlDriverNumber(sessionKey):
    url = f'https://api.openf1.org/v1/drivers?session_key={sessionKey}'
    dt = UrlToDataFrame(url)
    arr = dt['driver_number'].to_numpy()
    return arr

def GetIntervalData(sessionKey, driverNum):
    url = f'https://api.openf1.org/v1/intervals?session_key={sessionKey}&driver_number={driverNum}'
    return UrlToDataFrame(url)

def GetLapsData(sessionKey, driverNum = None):
    if driverNum:
        url = f'https://api.openf1.org/v1/laps?session_key={sessionKey}&driver_number={driverNum}'
    else:
        url = f'https://api.openf1.org/v1/laps?session_key={sessionKey}'
    return UrlToDataFrame(url)

def GetDriverLapsData(sessionKey, driverNum):
    url = f'https://api.openf1.org/v1/laps?session_key={sessionKey}&driver_number={driverNum}'
    return UrlToDataFrame(url)

def GetLocationData(sessionKey, driverNum):
    url = f'https://api.openf1.org/v1/location?session_key={sessionKey}&driver_number={driverNum}'
    return UrlToDataFrame(url)

def GetMeetingData(countryName, year):
    url = f'https://api.openf1.org/v1/meetings?year={year}&country_name={countryName}'
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

def GetStintsData(sessionKey, driverNum):
    url = f'https://api.openf1.org/v1/stints?session_key={sessionKey}&driver_number={driverNum}'
    return UrlToDataFrame(url)

def GetSessionDataByKey(sessionKey):
    url = f'https://api.openf1.org/v1/sessions?session_key={sessionKey}'
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

def GetSessionType(sessionKey):
    url = f'https://api.openf1.org/v1/sessions?session_key={sessionKey}'
    dt = UrlToDataFrame(url)
    return dt['session_type'][0]

#################### Specific Data Gathering  ####################

def DriverLapDuration(key, driverNum):
    url = f'https://api.openf1.org/v1/laps?driver_number={driverNum}&session_key={key}'
    dt =  UrlToDataFrame(url)
    dt = dt['lap_duration']
    return dt.mean()

def GetDriverInfo(key):
    url = f'https://api.openf1.org/v1/drivers?session_key={key}'
    dt = UrlToDataFrame(url)
    idx = random.choice(dt.index)
    dt = dt.loc[idx]
    dt = dt[['full_name', 'name_acronym',  'team_name', 'driver_number']]
    return dt


#################### Costumized Function ####################

def GetRandomDriver(sessionKey):
    data = GetDriverData(sessionKey)
    drivers = data['driver_number']

def GetTrackData(sessionKey):
    url = f'https://api.openf1.org/v1/sessions?session_key={sessionKey}'
    dt = UrlToDataFrame(url)
    dt = dt[['date_start', 'country_name', 'circuit_short_name', 'year', 'session_type', 'session_key']]
    return DataUtlis.FormatDate_DDMMYY(dt, 'date_start')

def RandomSessionKey():
    year = [2024, 2023]
    # year = [2023]
    dt = GetSessionData(random.choice(year), 'Race')
    return random.choice(dt['session_key'].to_numpy())

def RandomDriver(key):
    url = f'https://api.openf1.org/v1/drivers?session_key={key}'
    dt = UrlToDataFrame(url)
    idx = random.choice(dt.index)
    dt = dt.loc[idx]
    dt = dt[['full_name', 'name_acronym',  'team_name', 'driver_number']]
    return dt

def GetAllSessionKeys(year=None):
    keys = []
    temp = []
    if year:
        dt = GetSessionData(year, 'Race')
    else:
        dt1 = GetSessionData(2023, 'Race')
        dt2 = GetSessionData(2024, 'Race')
        dt = dt1._append(dt2, ignore_index=True)
    temp.append(dt['session_key'].values.tolist())
    for key in temp[0]:
        keys.append(key)
    return keys

def GetQualifyPosition(sessionKey):
    dt = ApiUtlis.GetPositionData(sessionKey)
    dt = dt.sort_values('date')
    final = dt.groupby('driver_number').last().reset_index()
    final.index += 1
    return final.sort_values('position')

def GetPosition(sessionKey):
    dt = ApiUtlis.GetPositionData(sessionKey)
    dt = dt.sort_values('date')
    dt = dt.groupby('driver_number').last().reset_index()
    dt.index += 1
    dt = dt.sort_values('position')
    dt = dt[['driver_number', 'position']]
    dt = DataUtlis.ResetIndex(dt)
    return dt




#################### All Data ####################

def GetAllTrackData():
    keys = GetAllSessionKeys()
    print(keys)
    tk = []
    for key in keys:
        dt = GetTrackData(key)
        tk.append(dt)
        time.sleep(0.2)
    return pd.concat(tk, ignore_index=True)



