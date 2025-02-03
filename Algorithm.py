import ApiUtlis
import DataUtlis
import math


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
    return sumNumer / denor

