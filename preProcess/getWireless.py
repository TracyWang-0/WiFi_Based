import pandas as pd
import os

wireless_filePath = '../data/raw/Wireless Indoor Localization Data Set/wifi_localization.txt'
wireless_out_filePath = '../data/out/Wireless_wifi_dataset.csv'

all_data = []
for line in open(wireless_filePath):
    items = line[:-1].split('\t')
    all_data.extend([items])

all_data = pd.DataFrame(all_data)
all_data.columns = ['WAP0', 'WAP1', 'WAP2', 'WAP3', 'WAP4', 'WAP5', 'WAP6', 'spaceID']
print(f'all_data.shape:{all_data.shape}')

all_data.to_csv(wireless_out_filePath, index=False)
