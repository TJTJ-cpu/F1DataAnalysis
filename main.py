from DataUtlis import *
from DriverData import GetDriverData
import DataUtlis

meeting_code = 1244
meeting_key = f'meeting_key={meeting_code}'

driverNumber = 16
driverKey = f'driver_number={driverNumber}'

sessionCode = 9590
sessionKey = f'session_key={sessionCode}'

dt = GetCarData(driverNumber, sessionCode)
dt = dt[['driver_number', 'date', 'n_gear', 'rpm', 'speed']]
ExportToExcel('CarData', dt)
print(dt)

