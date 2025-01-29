from pandas.core.arrays.datetimelike import datetimelike_accumulations
import DataUtlis 
import ApiUtlis
import DataUtlis

meeting_code = 1244
meeting_key = f'meeting_key={meeting_code}'

driverNumber = 16
driverKey = f'driver_number={driverNumber}'

sessionCode = 9590
sessionKey = f'session_key={sessionCode}'

# dt = ApiUtlis.GetLocationData(driverNumber, sessionCode)
dt = ApiUtlis.GetWeatherData(sessionCode)
print(dt)
# dt = dt[['driver_number', 'date', 'n_gear', 'rpm', 'speed']]
# dt = DataUtlis.ConvertTimeToSecond(dt, 'date')
DataUtlis.ExportToExcel('CarData', dt)
# print(dt)

