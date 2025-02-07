from pandas.core.series import algorithms
from enum import Enum

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import Algorithm
import ApiUtlis
import DataUtlis
import time
import os
import random

# keys = ApiUtlis.GetAllSessionKey()
# key = random.choice(keys)



# Age and Weight
data = [[12, 42], [13, 46], [14, 48], [15, 52], [16, 54], [17, 54], [18, 57], [19, 57], [20, 58]]

data2 = [[30, 80], [31, 88], [33, 90], [35, 95]]

# Category Type
class Category(Enum):
    CarData = "CarData"
    Laps = "Laps"
    RaceControl = "RaceControl"



# data = ApiUtlis.GetALlDriverNumber(key)
# driver = random.choice(data)

raceName = "Japan"
year = 2024

fileName = f'{raceName}_{year}'

cat = Category.CarData.value

path = os.path.join('Data', fileName, cat)
arr = os.listdir(path)

df = DataUtlis.ReadPitData(fileName, 16)
print(df)

# Algorithm.FullDataGatheringFunc()


