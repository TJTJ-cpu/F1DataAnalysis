import pandas as pd
import numpy as np
from pandas.core.series import algorithms

import matplotlib.pyplot as plt

import Algorithm
import ApiUtlis
import DataUtlis
import time
import random

keys = ApiUtlis.GetAllSessionKey()
key = random.choice(keys)

dt = ApiUtlis.GetQualifyPosition(key)
dt = dt[['driver_number', 'position']]
dt = DataUtlis.ResetIndex(dt)

val = ApiUtlis.GetSessionType(key)
dt = DataUtlis.AddNewColumn(dt, val, 'session_type')

dn = ApiUtlis.GetDriverData(key)
driverName = dn[['driver_number', 'name_acronym']]

pos = ApiUtlis.GetPosition(key)
track = ApiUtlis.GetTrackData(key)

# driver = ApiUtlis.RandomDriver(key)
# driverlapDura = ApiUtlis.DriverLapDuration(key, driver['driver_number'])

# print(track)
# print(pos)
dt = pos
posArr = []
duraArr = []

data = [[12, 42], [13, 46], [14, 48], [15, 52], [16, 54], [17, 54], [18, 57], [19, 57], [20, 58]]
df = pd.DataFrame(data, columns=['Age', 'Weight'])


# r = Algorithm.PearsonCorrelation(df, 'Age', 'Weight')
# print(r)

# print(df)

for index, row in pos.iterrows():
    driverNum = row.iloc[0]
    position = row.iloc[1]
    dura = ApiUtlis.DriverLapDuration(key, driverNum)
    duraArr.append(dura)
    # print(f'num: {driverNum}   pos: {position}   dura: {dura}')

print(track)

dt['duration'] = duraArr
vis =dt.plot.scatter(x='position', y='duration')
print(dt)
r = Algorithm.PearsonCorrelation(dt, 'position', 'duration')
print(f'r val: {r}')

plt.show()

# print(pos)
# print(driverlapDura)


# print(merge)

