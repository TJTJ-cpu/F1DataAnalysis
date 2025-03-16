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

Algorithm.FullDataGatheringFunc()

folders = DataUtlis.GetAllFolderNames()
# print(f'Folders: {len(folders)}')
corrDict = {}
spearDict = {}
kendallDict = {}
all_data = []

for f in folders:
    df = Algorithm.LapsTimevsPosition(f)

    if df is None:
        print("-" * 50)
        print(f'{f} has no data')
        print("-" * 50)
        continue

    all_data.append(df)

    # Calculate Correlations
    pearson_corr = df['position'].corr(df['avg_lap_duration'], method='pearson')
    spearman_corr = df['position'].corr(df['avg_lap_duration'], method='spearman')
    kendall_corr = df['position'].corr(df['avg_lap_duration'], method='kendall')

    # Store data in dict
    corrDict[f] = pearson_corr
    spearDict[f] = spearman_corr
    kendallDict[f] = kendall_corr

    print("-" * 50)
    print(f"Track: {f}")
    print(f"Pearson: {pearson_corr:.4f}")
    print(f"Spearman: {spearman_corr:.4f}")
    print(f"Kendall: {kendall_corr:.4f}")
    print("-" * 50)
# Sample Graph
DataUtlis.DisplayLineGraph(corrDict, 'Pearson: Between Position vs Avg Lap Duration')
DataUtlis.DisplayLineGraph(spearDict, 'Spearman: Between Position vs Avg Lap Duration')
DataUtlis.DisplayLineGraph(kendallDict, 'Kendall: Between Position vs Avg Lap Duration')


# find avg pos and high low temperature
final_df = pd.concat(all_data, ignore_index=True)
median_temp = final_df['air_temperature'].median()

# print(f'median temp: {median_temp}')
final_df['temperature'] = final_df['air_temperature'].apply(lambda x: 'High' if x > median_temp else 'Low')

# get avg finish p;os
driver_performance = final_df.groupby(['driver_number', 'temperature'])['position'].mean().reset_index()

driverDf = driver_performance.pivot(index='driver_number', columns='temperature', values='position')
# Fill missing values in case a driver didn't race in both conditions
driverDf = driverDf.fillna(np.nan)
driverDf.reset_index(inplace=True)

# name
driver_names = ApiUtlis.driver_names
driverDf['Driver Name'] = driverDf['driver_number'].map(driver_names)

# add diff column
driverDf['Performance_Difference'] = driverDf['Low'] - driverDf['High']

# Display the updated DataFrame

# Sort drivers by performance difference (ascending)
driverDf_sorted = driverDf.sort_values(by='Performance_Difference', ascending=True)
print(driverDf)


# visualization
driver_pivot_sorted = driverDf.sort_values(by='Performance_Difference', ascending=True)

# Define colors: Red = better in hot weather, Blue = better in cold weather
colors = ['red' if x < 0 else 'blue' for x in driver_pivot_sorted['Performance_Difference']]

# Plot Horizontal Bar Chart
plt.figure(figsize=(10, 6))
plt.barh(driver_pivot_sorted.index, driver_pivot_sorted['Performance_Difference'], color=colors)

plt.axvline(0, color='black', linewidth=1)  # Reference line at 0
plt.xlabel("Performance Difference (Low Temp - High Temp)")
plt.ylabel("Driver Number")
plt.title("Which Drivers Perform Better in Hot vs. Cold Weather?")

plt.show()


# for val in raceTemp.values():
#     print(val)
#     print(df)
#     if df is None:
#         print(f'{f} has no information')
#         print()
#     else:
#         # print(f)
#         corr = df['position'].corr(df['avg_lap_duration'])
#         spearCorr = df['position'].corr(df['avg_lap_duration'], method='spearman')
#         kendallCorr = df['position'].corr(df['avg_lap_duration'], method='kendall')
#         corrDict[f] = corr
#         spearDict[f] = corr
#         kendallDict[f] = corr
#         print(f)
#         time.sleep(3)
#         print(f'Pearson: {corr}')
#         time.sleep(1)
#         print(f'Spearman: {spearCorr}')
#         time.sleep(1)
#         print(f'Kendall: {kendallCorr}')
#         time.sleep(1)
#         print()
#
#
#         print(corr)
#         Bandate for this situation
#         Remove the 2 that we did not want anyway
#         if corr > -0.5:
#         else:
#             print(f)
#             print(df)
#             print(corr)
#             print('-----------------------------------------------------------------')
#
#
# correlations = list(corrDict.values())
# # Sample Graph
# DataUtlis.DisplayLineGraph(corrDict, 'Pearson: Between Position vs Avg Lap Duration')
# DataUtlis.DisplayLineGraph(spearDict, 'Spearman: Between Position vs Avg Lap Duration')
# DataUtlis.DisplayLineGraph(kendallDict, 'Kendall: Between Position vs Avg Lap Duration')


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


