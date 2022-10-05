import websocket, json, pprint, numpy
from binance.client import Client
from binance.enums import *
import numpy as np
import datetime
import math
import BKeys
import time
from concurrent import futures

print("---------------------Process Initiated---------------------")

client = Client(BKeys.API_KEY, BKeys.API_SECRET)
# print(dir(Client))
# asset_details = client.get_asset_details()
# exchange_info = client.get_exchange_info()

symbols = []
symbols_lower = []
usdt_symbols = []
snap = client.get_orderbook_tickers()

tmp = {}
for i in snap:
    tmp[i["symbol"]] = i

for i in snap:
    symbols.append(i["symbol"])
    symbols_lower.append(i["symbol"].lower())
    if "USDT" in i["symbol"] and (
        "UP" not in i["symbol"]
        and "DOWN" not in i["symbol"]
        and "BULL" not in i["symbol"]
        and "BEAR" not in i["symbol"]
    ):
        usdt_symbols.append(i["symbol"])
