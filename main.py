from DataUtlis import *
import DataUtlis
import DriverData

meeting_code = 1244
meeting_key = f'meeting_key={meeting_code}'

driverNumber = 16
driverKey = f'driver_number={driverNumber}'

sessionCode = 9590
sessionKey = f'session_key={sessionCode}'


driverName = DriverData.GetDriverData(driverNumber, sessionCode)

allSess = GetAllSessionCode(2024)
ExportToExcel('RaceKey', allSess)
print(allSess)


