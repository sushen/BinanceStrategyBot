from pprint import pprint

import talib
from dataframe.dataframe import GetDataframe
from sound.ringbell import Ring
from binance.helpers import round_step_size


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

    def buy_futures_contract(self, symbol):
        sell = input("Type 'Yes' :")
        print(sell)
        if sell == "Yes":
            APICall.client.futures_create_order(symbol=symbol, side='BUY', type='MARKET', quantity=99)
            print(input("Done Buying :"))
        else:
            print("Technical indicator is not right")
        return symbol

    def sell_futures_contract(self, symbol):
        sell = input("Type 'Yes' :")
        print(sell)
        if sell == "Yes":
            APICall.client.futures_create_order(symbol=symbol, side='SELL', type='MARKET', quantity=99)
            print(input("Done Buying :"))
        else:
            print("Technical indicator is not right")
        return symbol

    def buying_signal(self, symbol):
        if self.moving_average(symbol, "90") > self.moving_average(symbol, "25") > self.moving_average(symbol, "7"):
            print(f"Buy/Long : {symbol}")
            # Ring().play_long_sound('../sound/Sample.wav')
            # print(input("Stop Sound or Lower the volume:"))
            self.buy_futures_contract(symbol)
            return symbol
        elif self.moving_average(symbol, "90") < self.moving_average(symbol, "25") < self.moving_average(symbol, "7"):
            print(f"Sell/Short : {symbol}")
            # Ring().play_long_sound('../sound/Sample.wav')
            # print(input("Stop Sound or Lower the volume:"))
            self.sell_futures_contract(symbol)
            return symbol
        else:
            print(f"Asset {symbol} have no position for Buy/Sell")


import pandas as pd
from api_callling.api_calling import APICall


from get_symbol.find_symbols import FindSymbols
fs = FindSymbols()
feature = Feature()

futures_exchange_info = APICall.client.futures_exchange_info()
trading_pairs = [info['symbol'] for info in futures_exchange_info['symbols']]


def feature_coin_buying_signal():
    ticker_info = pd.DataFrame(APICall.client.get_ticker())
    all_symbol = fs.get_all_symbols("BUSD", ticker_info)
    for symbol in all_symbol["symbol"]:
        string = symbol
        result = [word for word in trading_pairs if word in string]
        if len(result) != 0:
            feature.buying_signal(symbol)

    # print(input("stop :"))


feature_coin_buying_signal()


