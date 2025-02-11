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


cat = Algorithm.CCategory.CarData.value
#
# path = os.path.join('Data', fileName, cat)
# arr = os.listdir(path)
#
# df = DataUtlis.ReadPitData(fileName)

# folders = DataUtlis.GetAllFolderNames()
# for f in folders:
#     print(f)
#     df = Algorithm.LapsTimevsPosition(f)
#     corr = df['position'].corr(df['avg_lap_duration'])
#     print(corr)
#     print()



# print(lapsDf)



# DO THIS AT NIGHT!
start = time.time()
while True:
    Algorithm.FullDataGatheringFunc()
Algorithm.FullDataGatheringFunc()
end = time.time()
elapsedTime = end - start
print(f'TimeTaken: {elapsedTime}')


