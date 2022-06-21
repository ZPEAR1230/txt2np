"""思路：读取数据---转换数据格式dataframe----取数：几行几列-----存储"""
"""文件读取顺序：1开始，然后2，然后3"""
import numpy as np
import pandas as pd
import glob
files = glob.glob('txt/water/*.txt')
r = []
for file in files:
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.readlines()
    print(file)
    li = [each.split() for each in data]
    df_data = pd.DataFrame(li)
    ds = df_data.iloc[:158, 3]
    r1 = []

    for i in range(len(ds)):
        r1.append(ds[i])
    # print(r1)
    r .append(r1)





np.save('numpy/water.npy',r)
res = []
f1 = np.load('numpy/water.npy',allow_pickle=True)
f2 = np.load('numpy/water.npy',allow_pickle=True)
res = np.append(f1,f2,axis=0)
res = np.append(res,f1,axis=0)
res = np.append(res,f1,axis=0)
res = np.append(res,f1,axis=0)

print(res.shape)

print(f1)

np.save('numpy/water_300.npy',res)


