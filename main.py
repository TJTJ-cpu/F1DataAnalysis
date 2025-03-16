import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import Algorithm
import ApiUtlis
import DataUtlis

# Algorithm.FullDataGatheringFunc()

folders = DataUtlis.GetAllFolderNames()
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

driverDf_sorted = driverDf.sort_values(by='Performance_Difference', ascending=True)
print(driverDf)


# visualization
driver_pivot_sorted = driverDf.sort_values(by='Performance_Difference', ascending=True)

colors = ['red' if x < 0 else 'blue' for x in driver_pivot_sorted['Performance_Difference']]

plt.figure(figsize=(10, 6))
plt.barh(driver_pivot_sorted.index, driver_pivot_sorted['Performance_Difference'], color=colors)

plt.axvline(0, color='black', linewidth=1)  # Reference line at 0
plt.xlabel("Performance Difference (Low Temp - High Temp)")
plt.ylabel("Driver Number")
plt.title("Which Drivers Perform Better in Hot vs. Cold Weather?")

plt.show()
