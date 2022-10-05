from trade_utils import *
from cache import *
import pandas as pd
import numpy as np

# from Data_retreival import *


# Test for a single case

# start = '2020-01-01'
# PERIOD = ['4hr']
# usdt_symbols = ['BTCUSDT']
# for g in PERIOD:
#     for i in usdt_symbols:
#         df = pd.read_csv(f'./data/{g}/{i}_{g}.csv')
#         df = df[df['Unnamed: 0']>=start]
#         df = generate_returns(df)
#         df = generate_sma(df,start = 2,end=700,step=1)
#         data = calculate_returns(df,40,50,120)
#         bnh = np.array(data['bnh'])[-1]
#         sret = np.array(data['s_returns'])[-1]
#         print(sret/bnh)

# start = '2020-01-01'
# df = pd.read_csv(f'./data/4hr/BTCUSDT_4hr.csv')
# df = df[df['Unnamed: 0']>=start]
# df = df.reset_index()
# # df = df.drop(df.index)
# print(df.head())
# print(df['symbol'][0])

# Bulk Optimization

start = "2018-01-01"
end = "2022-03-19"
# PERIOD = ['day','4hr','week','month']
PERIOD = ["15m"]
usdt_symbols = [
    "RUNEUSDT",
    "BNBUSDT",
    "BTCUSDT",
    "MIRUSDT",
    "WAVESUSDT",
    "SOLUSDT",
    "IOTXUSDT",
    "RNDRUSDT",
    "BATUSDT",
    "GXSUSDT",
    "CTXCUSDT",
    "STXUSDT",
    "VETUSDT",
    "KNCUSDT",
    "LUNAUSDT",
    "POLSUSDT",
    "ADAUSDT",
    "MANAUSDT",
    "SANDUSDT",
    "GALAUSDT",
]
for g in PERIOD:
    out_file = f"croc_portfolio_2021_{g}.txt"
    for i in usdt_symbols:
        df = pd.read_csv(f"./data1/{g}/{i}_{g}.csv")
        print(df.columns)
        print(df.symbol[0])
        df["Date"] = pd.to_datetime(df["Unnamed: 0"])
        df = df[df["Date"] >= start]
        df = df[df["Date"] <= end]
        df = generate_returns(df)
        df = generate_sma(df, start=2, end=300, step=1)
        # print(df.head())
        # print(df.tail())
        optimize(df, out_file)

# print('Buy and hold returns:', np.array(data['bnh'])[-1])
# print('Strategy returns:', np.array(data['s_returns'])[-1])
