from urllib.request import urlopen
import pandas as pd
import json
import DriverData

baseUrlPos = 'https://api.openf1.org/v1/position?'
baseUrlLaps = 'https://api.openf1.org/v1/laps?'

meeting_code = 1244
meeting_key = f'meeting_key={meeting_code}'

driverNumber = 18
driverKey = f'driver_number={driverNumber}'

sessionCode = 9590
sessionKey = f'session_key={sessionCode}'


posUrl = f'{baseUrlPos}&{meeting_key}&{driverKey}&{sessionKey}'
lapsUrl = f'{baseUrlLaps}&{sessionKey}&{driverKey}'


response = urlopen(posUrl)
data = json.loads(response.read().decode('utf-8'))
positionData = pd.DataFrame(data)

response = urlopen(lapsUrl)
data = json.loads(response.read().decode('utf-8'))
lapsData = pd.DataFrame(data)

outputFile = 'F1Data.xlsx'
lapsData.to_excel(outputFile, index=False)

pairData = dict(zip(lapsData['lap_number'], lapsData['lap_duration']))
totalLapdurations = pairData

totalTime = 0

totalLapdurations = lapsData.dropna(subset=['lap_duration'])

for duration in totalLapdurations['lap_duration']:
    totalTime += duration

totalLapNum = lapsData['lap_number'].max()
driver = DriverData.GetDriverName(driverNumber)

# Print Station
print(f"{driver} : {totalTime / totalLapNum}")
# print(lapsData.columns)



