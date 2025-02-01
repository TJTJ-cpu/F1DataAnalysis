from ssl import ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN
import pandas as pd
import numpy as np

import ApiUtlis
import DataUtlis
import time
import random

meeting_code = 1244
meeting_key = f'meeting_key={meeting_code}'

driverNumber = 16
driverKey = f'driver_number={driverNumber}'

sessionCode = 9590
sessionKey = f'session_key={sessionCode}'


keys = ApiUtlis.GetAllSessionKey()

# Export All PositionData
# for key in keys:
#     data = ApiUtlis.GetPositionData(key)
#     dt = DataUtlis.FormatTime_HHMMSS(data, 'date')
#     DataUtlis.ExportPositionData(dt, key)

key = random.choice(keys)
# dt = ApiUtlis.GetSessionData(2024, 'Qualifying')

qualiExample = 9562

# print(ApiUtlis.GetTrackData(qualiExample))

dt = ApiUtlis.GetQualifyPosition(qualiExample)
dt = dt[['driver_number', 'position']]
# print(dt)

dn = ApiUtlis.GetDriverData(qualiExample)
# print(dn.columns)
test = dn[['driver_number', 'broadcast_name']]
# print(test)

merge = DataUtlis.MergeDataFrame(test, dt, 'driver_number')
merge = merge.sort_values('position')
print(merge)

# pos = ApiUtlis.GetPositionData(9468)
# print(pos)

# Get everything
# for key in keys:
#     dt = ApiUtlis.GetTrackData(key)
#     tk.append(dt)
#     time.sleep(0.2)

# for x in range(10):
#     dt = ApiUtlis.GetSessionData(2023, 'Race')
#     arr = dt['session_key'].to_numpy()
#     key = ApiUtlis.RandomSessionKey()
#     dt = ApiUtlis.GetTrackData(key)
#     tk.append(dt)



# DataUtlis.ExportToExcel('F1Data', dt)
# print(dt)


# dt = ApiUtlis.GetCarData(sessionCode, driverNumber)
# dt = dt[['driver_number', 'date', 'n_gear', 'rpm', 'speed']]
# dt = DataUtlis.FormatTime_HHMMSS(dt, 'date')
# dt = DataUtlis.RemoveRowIfZero(dt, 'n_gear')
# DataUtlis.ExportToExcel('CarData', dt)
# print(dt)

