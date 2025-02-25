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

#GET RANDOM SESSION KEY
keys = ApiUtlis.GetAllSessionKeys()
key = random.choice(keys)


# Age and Weight
data = [[12, 42], [13, 46], [14, 48], [15, 52], [16, 54], [17, 54], [18, 57], [19, 57], [20, 58]]

data2 = [[30, 80], [31, 88], [33, 90], [35, 95]]

# data = ApiUtlis.GetALlDriverNumber(key)
# driver = random.choice(data)

fileName = random.choice(DataUtlis.GetAllFolderNames())
# print(fileName)

# for key in keys:
#     dt = ApiUtlis.GetTrackData(key)
#     print(dt)

# TO GATHER ALL THE INFORMATION
# while True:
# Algorithm.FullDataGatheringFunc()

#To code list
#Qualifying position vs. race result 

folders = DataUtlis.GetAllFolderNames()
print(len(folders))
corrDict = {}
for f in folders:
    df = Algorithm.LapsTimevsPosition(f)
    if df is None:
        print(f'{f} has no information')
    else:
        # print(f)
        corr = df['position'].corr(df['avg_lap_duration'])
        corrDict[f] = corr

for x, y in corrDict.items():
    print(x, y)

# DataUtlis.DisplayGraph(lowCorrDf, "Low Corr")
# DataUtlis.DisplayGraph(highCorrDf, "High Corr")
# for x in lowCorrDf:
#     print(x)

# print(ApiUtlis.GetTrackData(key))
# df = ApiUtlis.GetPositionData(key)
# drivers = ApiUtlis.GetALlDriverNumber(key)
# for driver in drivers:
#     temp = ApiUtlis.GetDriverLapsData(key, driver)
#     print(temp)
    # temp = DataUtlis.RemoveNanRows(temp)
    # print(f'DriverNum: {driver}, Laps Count: {len(temp)}')


# high = 'Netherlands_2024'
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
# Algorithm.FullDataGatheringFunc()
# end = time.time()
# elapsedTime = end - start
# print(f'TimeTaken: {elapsedTime}')


