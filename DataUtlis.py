from urllib.request import urlopen
import pandas as pd
import json


def ExportToExcel(fileName, Data):
    Data.to_excel(f'{fileName}.xlsx', index=False)


def GetAllSessionCode(year):
    sessionBaseUrl = 'https://api.openf1.org/v1/sessions?session_name=Race'
    sessionUrl = f'{sessionBaseUrl}&year={year}'

    sessionData = UrlToDataFrame(sessionUrl)
    # Change the date format
    sessionData['date_start'] = pd.to_datetime(sessionData['date_start']).dt.strftime('%d-%m-%Y')
    # print(sessionData.columns)
    return sessionData[['session_key', 'country_name', 'circuit_short_name', 'date_start']]


def UrlToDataFrame(url):
    response = urlopen(url)
    dt = json.loads(response.read().decode('utf-8'))
    Data  = pd.DataFrame(dt)
    return Data
