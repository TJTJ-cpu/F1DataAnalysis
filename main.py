from urllib.request import urlopen
import pandas as pd
import json

baseUrl = 'https://api.openf1.org/v1/position?'

meeting_code = 1244
meeting_key = f'meeting_key={meeting_code}'

driverNumber = 1
driverKey = f'driver_number={driverNumber}'

sessionCode = 9590
sessionKey = f'session_key={sessionCode}'



finalUrl = f'{baseUrl}&{meeting_key}&{driverKey}&{sessionKey}'

response = urlopen(finalUrl)
data = json.loads(response.read().decode('utf-8'))
df = pd.DataFrame(data)

outputFile = 'F1Data.xlsx'
df.to_excel(outputFile, index=False)

print(df)

