import pandas as pd
import numpy as np

def process_save_all_data(Hybrid_all_out_filePath):
    Hybrid_raw_filePath = '../data/raw/Hybrid Indoor Positioning Dataset/dataset.csv'
    Hybrid_raw_Data = pd.read_csv(Hybrid_raw_filePath)
    print(f'Hybrid_raw_Data.shape:{Hybrid_raw_Data.shape}')

    hybrid_data = []

    # 获取属性名，并去掉多于的引号
    headers = str(Hybrid_raw_Data.columns.values[0]).split(';')
    for idx, attr in enumerate(headers[1:]):
        headers[idx+1] = eval(attr)
    hybrid_data = [headers]

    # 获取每一行，依旧去掉多余的引号
    for item in Hybrid_raw_Data.to_numpy():
        items = str(item[0]).split(';')
        for idx, value in enumerate(items):
            if '"' in value:
                items[idx] = eval(value)

        hybrid_data.append(items)

    # 保存处理后的全部数据
    hybrid_data = pd.DataFrame(hybrid_data)
    hybrid_data.to_csv(Hybrid_all_out_filePath, header=None, index=False, index_label=None)

def learn_attrs(Hybrid_wifi_out_filePath):
    wifi_data = pd.read_csv(Hybrid_wifi_out_filePath)

    # 依次获取前7个属性，然后查看共有多少个
    for idx in range(7):
        attr = wifi_data.iloc[:, idx]
        x = np.unique(attr)
        print(x.shape)



if __name__ == '__main__':
    # 需要保存的文件位置
    Hybrid_all_out_filePath = '../data/out/Hybrid_all_dataset.csv'
    Hybrid_wifi_out_filePath = '../data/out/Hybrid_wifi_dataset.csv'

    # process_save_all_data(Hybrid_all_out_filePath)
    learn_attrs(Hybrid_wifi_out_filePath)
