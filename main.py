import pandas as pd
import numpy as np
import DataUtlis  
import ApiUtlis
import DataUtlis
import time

meeting_code = 1244
meeting_key = f'meeting_key={meeting_code}'

driverNumber = 16
driverKey = f'driver_number={driverNumber}'

sessionCode = 9590
sessionKey = f'session_key={sessionCode}'


tk = []
keys = ApiUtlis.GetAllSessionKey()

# ts = [1,2,3,4]
# print(ts[0])


for key in keys:
    dt = ApiUtlis.GetTrackData(key)
    tk.append(dt)
    time.sleep(0.2)

# for x in range(10):
#     dt = ApiUtlis.GetSessionData(2023, 'Race')
#     arr = dt['session_key'].to_numpy()
#     key = ApiUtlis.RandomSessionKey()
#     dt = ApiUtlis.GetTrackData(key)
#     tk.append(dt)

tracks = pd.concat(tk, ignore_index=True)
print(tracks)

# DataUtlis.ExportToExcel('F1Data', dt)
# print(dt)


# dt = ApiUtlis.GetCarData(sessionCode, driverNumber)
# dt = dt[['driver_number', 'date', 'n_gear', 'rpm', 'speed']]
# dt = DataUtlis.FormatTime_HHMMSS(dt, 'date')
# dt = DataUtlis.RemoveRowIfZero(dt, 'n_gear')
# DataUtlis.ExportToExcel('CarData', dt)
# print(dt)

