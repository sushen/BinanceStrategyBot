import re
from pprint import pprint

import talib

from dataframe.dataframe import GetDataframe


class Feature(GetDataframe):

    def data_pull(self, symbol, look_back):
        days_panda_data = self.get_minute_data(symbol, 1, look_back)
        close_column = days_panda_data['Close']
        # minute_panda_data = self.get_minute_data(symbol, 5, look_back)
        # close_column = minute_panda_data['Close']
        return close_column

    def moving_average(self, symbol, look_back):
        close_column = self.data_pull(symbol, look_back)
        real = talib.MA(close_column, timeperiod=int(look_back), matype=0).iloc[-1]
        # print(real)
        return real

    def buying_signal(self, symbol):
        if self.moving_average(symbol, "90") > self.moving_average(symbol, "25") > self.moving_average(symbol, "7"):
            print(f"buy {symbol}")
            # Ring().play_long_sound('../sound/Sample.wav')
            print(input("Stop Sound or Lower the volume:"))
            # return symbol
        else:
            print(f"Moving Average of {symbol} pass the limit")


import pandas as pd
from api_callling.api_calling import APICall


from get_symbol.find_symbols import FindSymbols
fs = FindSymbols()
feature = Feature()

ticker_info = pd.DataFrame(APICall.client.get_ticker())
# print(ticker_info)
all_symbol = fs.get_all_symbols("BUSD", ticker_info)
# print(all_symbol['symbol'])
# print(all_symbol['symbol'].iloc[0])
# print(input("Stop :"))
# print(feature.data_pull(all_symbol['symbol'].iloc[0], 30))

# feature.buying_signal(all_symbol['symbol'].iloc[0])

# feature.buying_signal('DNTBUSD')

futures_exchange_info = APICall.client.futures_exchange_info()
trading_pairs = [info['symbol'] for info in futures_exchange_info['symbols']]

# for symbol in trading_pairs:
#     print(symbol)

# print(trading_pairs)
# print(len(trading_pairs))


def moving_average_signal():
    ticker_info = pd.DataFrame(APICall.client.get_ticker())
    all_symbol = fs.get_all_symbols("BUSD", ticker_info)
    for symbol in all_symbol["symbol"]:
        # print(symbol)
        string = symbol

        result = [word for word in trading_pairs if word in string]
        # print(result)
        # print(len(result))
        if len(result) != 0:
            feature.buying_signal(symbol)
            # print(input("stop :"))

    print(input("stop :"))


moving_average_signal()


