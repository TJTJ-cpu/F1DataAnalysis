from DataUtlis import *
    

def GetDriverName(driverNum, sessionKey):
    driverBaseUrl = 'https://api.openf1.org/v1/drivers?'
    driverUrl = f'{driverBaseUrl}driver_number={driverNum}&session_key={sessionKey}'

    driverData = UrlToDataFrame(driverUrl)
    return driverData[['full_name', 'name_acronym']]



def GetDriverData(driverNum, sessionKey):
    driverBaseUrl = 'https://api.openf1.org/v1/drivers?'
    driverUrl = f'{driverBaseUrl}driver_number={driverNum}&session_key={sessionKey}'

    driverData = UrlToDataFrame(driverUrl)
    return driverData


