from ssl import ALERT_DESCRIPTION_INSUFFICIENT_SECURITY
import matplotlib.pyplot as plt
import pandas as pd

import ApiUtlis
import DataUtlis
import math
import random



#################### FullStackFunction ####################

def FS_Lap_Pos():
    # dataList = [[pos1, dura1], [pos2, dura2]]
    dataList = [[]]
    position = []
    duraArr = []
    tempList = [[]]
    keys = ApiUtlis.GetAllSessionKey()
    keys = [7779, 7953]
    for key in keys:
        # Get Keys
        print(key)
        df = ApiUtlis.GetPosition(key)
        tempList = [[]]

        # Track Info
        tk = ApiUtlis.GetTrackData(key)
        tkName = tk[['circuit_short_name', 'country_name', 'year']]
        print(tkName)

        # Iter
        for index, row in df.iterrows():
            driverNum = int(row.iloc[0])
            position = int(row.iloc[1])
            dura = ApiUtlis.DriverLapDuration(key, driverNum)
            temp = [position, float(dura)]
            print(temp)
            tempList.append([position, dura])

    # Spread Sheet
    df = pd.DataFrame(tempList, columns=['Age', 'Weight'])
    rVal = df['Age'].corr(df['Weight'])
    print(f'final rval: {rVal}')

    # print(dataList)
    # r val
    # plot 
    # df.plot.scatter(x='position', y='duration')
    # plt.show()

def FullExportFunction():
    keys = ApiUtlis.GetAllSessionKey()
    keysNum = len(keys)
    print(f'Race Count: {keysNum}')
    random.shuffle(keys)
    for i, key in enumerate(keys):
        trackData = ApiUtlis.GetTrackData(key)
        print(f'{i}. {trackData[['circuit_short_name', 'country_name']]}')
        # get driver number
        driverArr = ApiUtlis.GetALlDriverNumber(key)
        for driver in driverArr:
            data = ApiUtlis.GetCarData(key, driver)
            DataUtlis.ExportToExcel(f'CarData_{key}_{driver}', data, 'CarData')
        return
    return

#################### Algorithm  ####################
def PearsonCorrelation(dt, val1, val2):
    meanX = dt[val1].mean()
    meanY = dt[val2].mean()
    sumNumer = 0
    sumDenor1 = 0
    sumDenor2 = 0
    for index, row in dt.iterrows():
        xi = row.iloc[0]
        yi = row.iloc[1]
        numer = (xi - meanX)*(yi - meanY)
        denor1 = math.pow((xi - meanX),2)
        denor2 = math.pow((yi - meanY),2)
        sumNumer += numer
        sumDenor1 += denor1
        sumDenor2 += denor2
    denor = math.sqrt(sumDenor1 * sumDenor2)
    if denor == 0:
        return 0
    return sumNumer / denor

#############################################################
