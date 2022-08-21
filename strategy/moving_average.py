"""
This class indicate when you will buy the Currency.
We're buying signal return buy that will be the perfect time to enter the market.
Combine this class with after finding a pattern and before buying strategy give you amazing result.

"""

import talib

from dataframe.dataframe import GetDataframe
from sound.ringbell import Ring


class MovingAverage(GetDataframe):

    def data_pull(self, symbol, look_back):
        days_panda_data = self.get_day_data(symbol, 1, look_back)
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
moving_av = MovingAverage()


def moving_average_signal():
    ticker_info = pd.DataFrame(APICall.client.get_ticker())
    all_symbol = fs.get_all_symbols("BUSD", ticker_info)
    for symbol in all_symbol["symbol"]:
        moving_av.buying_signal(symbol)


for i in range(100):
    print(f"\nSearching {i} time.\n")
    moving_average_signal()







