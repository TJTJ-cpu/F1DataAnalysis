from pandas.core.dtypes.generic import ABCPeriodArray
from pandas.core.series import algorithms
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import Algorithm
import ApiUtlis
import DataUtlis
import time
import os
import random

keys = ApiUtlis.GetAllSessionKeys()
key = random.choice(keys)



# Age and Weight
data = [[12, 42], [13, 46], [14, 48], [15, 52], [16, 54], [17, 54], [18, 57], [19, 57], [20, 58]]

data2 = [[30, 80], [31, 88], [33, 90], [35, 95]]




# data = ApiUtlis.GetALlDriverNumber(key)
# driver = random.choice(data)

fileName = random.choice(DataUtlis.GetAllFolderNames())
# print(fileName)


# TO GATHER ALL THE INFORMATION
# while True:
#     Algorithm.FullDataGatheringFunc()

folders = DataUtlis.GetAllFolderNames()
for f in folders:
    df = Algorithm.LapsTimevsPosition(f)
    corr = df['position'].corr(df['avg_lap_duration'])
    # print(f'{f}  {corr}')
    # print(df)
    # print()

# print(ApiUtlis.GetTrackData(key))
# df = ApiUtlis.GetPositionData(key)
# drivers = ApiUtlis.GetALlDriverNumber(key)
# for driver in drivers:
#     temp = ApiUtlis.GetDriverLapsData(key, driver)
#     print(temp)
    # temp = DataUtlis.RemoveNanRows(temp)
    # print(f'DriverNum: {driver}, Laps Count: {len(temp)}')


# high = 'Spain_2024'
# avg = 'Mexico_2024'
# arr.append(avg)
# arr.append(high)
# low = 'Qatar_2023'
# arr.append(low)
#
# for f in arr:
#     df = Algorithm.LapsTimevsPosition(f)
#     d1 = df[df['driver_number'] == 16]
#     d2 = df[df['driver_number'] == 55]
#     corr = df['position'].corr(df['avg_lap_duration'])  # Compute correlation
    # if pd.isna(df.loc[df['driver_number'] == 55, 'avg_lap_duration']).any():
    #     print("Driver 55 has NaN in avg_lap_duration")
    # print(d1)
    # print(d2)


# print(lapsDf)



# DO THIS AT NIGHT!
# start = time.time()
# while True:
#     Algorithm.FullDataGatheringFunc()
# end = time.time()
# elapsedTime = end - start
# print(f'TimeTaken: {elapsedTime}')


