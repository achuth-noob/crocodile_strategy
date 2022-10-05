from cache import *
from datetime import datetime
import pandas as pd
import threading


period_socket = {
    # "week": Client.KLINE_INTERVAL_1WEEK,
    "day": Client.KLINE_INTERVAL_1DAY,
    # "month": Client.KLINE_INTERVAL_1MONTH,
    "4hr": Client.KLINE_INTERVAL_4HOUR,
    "1hr": Client.KLINE_INTERVAL_1HOUR,
    "15m": Client.KLINE_INTERVAL_15MINUTE,
    "5m": Client.KLINE_INTERVAL_5MINUTE,
    "1m": Client.KLINE_INTERVAL_1MINUTE,
    "30m": Client.KLINE_INTERVAL_30MINUTE,
    # "3m": Client.KLINE_INTERVAL_3MINUTE,
}


def get_historical_data(usdt_sym, period, socket):
    try:
        # pass
        time.sleep(1)
        klines = client.get_historical_klines(
            usdt_sym, socket, "19 Mar, 2000", "28 Apr, 2022"
        )
        tmp = {}
        for j in klines:
            tmp1 = {}
            tmp1["symbol"] = usdt_sym
            tmp1["Open"] = float(j[1])
            tmp1["High"] = float(j[2])
            tmp1["Low"] = float(j[3])
            tmp1["Close"] = float(j[4])
            tmp1["Volume"] = float(j[5])
            tmp[datetime.fromtimestamp(j[0] // 1000)] = tmp1
        tmp = pd.DataFrame(tmp).T
        # print(tmp)
        tmp.index = pd.to_datetime(tmp.index).date
        # tmp.to_csv(f'./data2/{period}/{usdt_sym}_{period}.csv', mode='a', index=True, header=False)
        tmp.to_csv(f'./data2/{period}/{usdt_sym}_{period}.csv')
        print(f"Data for {usdt_sym}_{period} retrieved......")
    except:
        print(f"Exception hit for {usdt_sym}_{period}")


def process(usdt_symbols, start, end, j, sock):
    for i in usdt_symbols[start:end]:
        # try:
        get_historical_data(i, j, sock)
        # except:
        #     print('Couldnt get i')


def split_processing(usdt_symbols, num_splits=10):
    for j in period_socket:
        split_size = len(usdt_symbols) // num_splits
        threads = []
        for i in range(num_splits):
            # determine the indices of the list this thread will handle
            start = i * split_size
            # special case on the last chunk to account for uneven splits
            end = None if i + 1 == num_splits else (i + 1) * split_size
            # create the thread
            threads.append(
                threading.Thread(
                    target=process, args=(usdt_symbols, start, end, j, period_socket[j])
                )
            )
            threads[-1].start()  # start the thread we just created

        # wait for all threads to finish
        for t in threads:
            t.join()


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

split_processing(usdt_symbols)


# usdt_symbols = ['BTCUSDT']
# usdt_symbols = ['BTCUSDT','ETHUSDT','BNBUSDT',\
#     'ADAUSDT','LTCUSDT','LINKUSDT']

# with futures.ThreadPoolExecutor(len(usdt_symbols)) as executor:
#     res = executor.map(get_historical_data,usdt_symbols)
