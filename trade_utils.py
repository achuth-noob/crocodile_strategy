import numpy as np
import json
import matplotlib.pyplot as plt
import threading


def ema(data, period):
    data[f"ema_{period}"] = data["Close"].ewm(span=period, adjust=False).mean()
    return data


def calculate_returns(data, sma, mma, lma):
    data = backtest_strategy(data, sma, mma, lma)
    data = data.dropna()
    data["bnh"] = (np.array(data["p_returns"]) + 1).cumprod()
    data["s_returns"] = (np.array(data["strategy_returns"] + 1)).cumprod()
    # plt.figure(figsize=(10,6))
    # plt.plot(data['bnh'])
    # plt.plot(data['s_returns'])
    # plt.ylabel('Cumulative Returns')
    # plt.xlabel('Timestamp')
    # plt.title('Returns Comparison')
    # plt.legend()
    # plt.show()
    return data


# def compute_strategy_returns(data,FEMA,MEMA,SEMA):
#     returns = 0
#     data = backtest_strategy(data,FEMA,MEMA,SEMA)
#     data['strategy_returns'] = np.where(data['position']*data['Daily_returns']!=0,data['position']*data['Daily_returns'],1).cumprod()
#     returns = np.where(data['position']*data['Daily_returns']!=0,data['position']*data['Daily_returns'],1).cumprod()[-1]
#     print(f'Strategy Returns with combination {[FEMA,MEMA,SEMA]} : {(returns-1)*100}%')
#     return data


def generate_returns(data):
    print(data)
    data["p_returns"] = data["Close"].pct_change()
    return data


def generate_sma(data, start=2, end=300, step=1):
    print(data)
    for i in range(start, end, step):
        print(f"Calculating {i} ma.......")
        data[f"ma_{i}"] = data["Close"].rolling(window=i).mean()
    return data


def backtest_strategy(df, sma, mma, lma):
    data = df.copy()
    data["signal"] = np.where(
        (data["Close"] > data[f"ma_{sma}"])
        & (data["Close"] > data[f"ma_{mma}"])
        & (data["Close"] > data[f"ma_{lma}"]),
        1,
        0,
    )

    data["signal"] = np.where(
        (data["Close"] < data[f"ma_{sma}"]) & (data["Close"] > data[f"ma_{lma}"]),
        0,
        data["signal"],
    )

    data["signal"] = np.where(
        (data["Close"] < data[f"ma_{sma}"])
        & (data["Close"] < data[f"ma_{mma}"])
        & (data["Close"] < data[f"ma_{lma}"]),
        -1,
        data["signal"],
    )

    data["signal"] = np.where(
        (data["Close"] > data[f"ma_{sma}"]) & (data["Close"] < data[f"ma_{lma}"]),
        0,
        data["signal"],
    )

    data["strategy_returns"] = data["p_returns"] * data["signal"].shift(1)
    return data


# def process(items, start, end):
#     for item in items[start:end]:
#         try:
#             api.my_operation(item)
#         except Exception:
#             print("error with item")


# def split_processing(items, num_splits=4):
#     split_size = len(items) // num_splits
#     threads = []
#     for i in range(num_splits):
#         # determine the indices of the list this thread will handle
#         start = i * split_size
#         # special case on the last chunk to account for uneven splits
#         end = None if i + 1 == num_splits else (i + 1) * split_size
#         # create the thread
#         threads.append(threading.Thread(target=process, args=(items, start, end)))
#         threads[-1].start()  # start the thread we just created

#     # wait for all threads to finish
#     for t in threads:
#         t.join()


# split_processing(items)


def optimize(data, out_file):
    max_returns = -10000.000
    comb = [0, 0, 0]
    data = data.dropna()
    data = data.reset_index()
    # print(data)
    df = data.copy()
    print(df.symbol[0])
    try:
        for sma in range(22, 23, 1):
            for mma in range(sma + 20, 43, 1):
                for lma in range(mma + 40, 84, 1):
                    print(f"\nChecking for SMA: {sma}, MMA: {mma}, LMA: {lma}")
                    df = data.copy()
                    df = calculate_returns(df, sma, mma, lma)
                    print(df.symbol[1])
                    bnh = np.array(df["bnh"])[-1]
                    sret = np.array(df["s_returns"])[-1]
                    # print('Buy and hold returns:', bnh)
                    # print('Strategy returns:', sret)
                    if max_returns < sret / bnh:
                        max_returns = sret / bnh
                        comb = [sma, mma, lma]
        else:
            print(f"Max returns possible : {max_returns}")
            print(f"Combination : {comb}")
            dic = {
                "symbol": df.symbol[1],
                "Time_period": "Full",
                "opt_comb": comb,
                "max_returns": max_returns,
            }
            with open(f"./data/{out_file}", "a") as f:
                f.write(str(dic) + "\n")
            f.close()
            print("Computation Completed.")
    except:
        print(f"Exception hit for {df.symbol[1]}")
