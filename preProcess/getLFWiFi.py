import os
import pandas as pd
import numpy as np

f_rawRoot = '../data/raw'

def processUJIndoorLoc(dir):
    dir = os.path.join(f_rawRoot, dir)
    f_train = os.path.join(dir, 'trainingData.csv')
    f_validation = os.path.join(dir, 'validationData.csv')

    rawTrain = pd.read_csv(f_train)
    rawValidation = pd.read_csv(f_validation)

    # 统计PHONEID
    # print(np.unique(rawTrain['PHONEID']))               # [ 1  3  6  7  8 10 11 13 14 16 17 18 19 22 23 24]
    # print(np.unique(rawValidation['PHONEID']))          # [ 0  2  4  5  9 12 13 14 15 20 21]
    # print(np.unique(rawTrain['PHONEID']).shape)         # (16,)
    # print(np.unique(rawValidation['PHONEID']).shape)    # (11,)

    # 统计USERID
    # print(np.unique(rawTrain['USERID']))               # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18]
    # print(np.unique(rawValidation['USERID']))          # [0]
    # print(np.unique(rawTrain['USERID']).shape)         # (18,)
    # print(np.unique(rawValidation['USERID']).shape)    # (1,)

    # 统计SPACEID
    # print(np.unique(rawTrain['SPACEID']))               #
    # print(np.unique(rawValidation['SPACEID']))          # [0]
    # print(np.unique(rawTrain['SPACEID']).shape)         # (123,)
    # print(np.unique(rawValidation['SPACEID']).shape)    # (1,)

    # 统计RELATIVEPOSITION
    # print(np.unique(rawTrain['RELATIVEPOSITION']))               # [1 2]
    # print(np.unique(rawValidation['RELATIVEPOSITION']))          # [0]
    # print(np.unique(rawTrain['RELATIVEPOSITION']).shape)         # (2,)
    # print(np.unique(rawValidation['RELATIVEPOSITION']).shape)    # (1,)

    # 统计BUILDINGID
    # print(np.unique(rawTrain['BUILDINGID']))               # [0 1 2]
    # print(np.unique(rawValidation['BUILDINGID']))          # [0 1 2]
    # print(np.unique(rawTrain['BUILDINGID']).shape)         # (3,)
    # print(np.unique(rawValidation['BUILDINGID']).shape)    # (3,)

    # print(rawTrain.shape)                               # (19937, 529)
    # print(rawValidation.shape)                          # (1111, 529)

    # print(rawTrain.columns.values.tolist())


def processIPIN2016():
    pass

if __name__ == '__main__':
    processUJIndoorLoc('UJIndoorLoc')