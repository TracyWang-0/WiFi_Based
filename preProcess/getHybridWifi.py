import pandas as pd
import numpy as np

Hybrid_raw_filePath = '../data/raw/Hybrid Indoor Positioning Dataset/dataset.csv'
Hybrid_out_filePath = '../data/out/Hybrid_dataset.csv'


Hybrid_raw_Data = pd.read_csv(Hybrid_raw_filePath)
print(f'Hybrid_raw_Data.shape:{Hybrid_raw_Data.shape}')

hybrid_data = []

hybrid_data = str(Hybrid_raw_Data.columns.values).split(';')

for item in Hybrid_raw_Data.to_numpy():
    items = str(item).split(';')
    hybrid_data.append(items)

hybrid_data = np.array(hybrid_data)
print(f'hybrid_data.shape:{hybrid_data.shape}')

hybrid_data.tofile(Hybrid_out_filePath, ',')

