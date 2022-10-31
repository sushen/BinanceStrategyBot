import talib
from dataframe.dataframe import GetDataframe
from feature_buy_sell.futures_buy_sell import FuturesBuySell


class OneMinuteMA(GetDataframe, FuturesBuySell):
    def one_minutes_data_pull(self, symbol, look_back):
        days_panda_data = self.get_minute_data(symbol, 1, look_back)
        close_column = days_panda_data['Close']
        return close_column

    def one_minutes_moving_average(self, symbol, look_back):
        close_column = self.one_minutes_data_pull(symbol, look_back)
        real = talib.MA(close_column, timeperiod=int(look_back), matype=0).iloc[-1]
        print(real)
        return real

    def one_minutes_buying_signal(self, symbol):
        if self.one_minutes_moving_average(symbol, "90") > self.one_minutes_moving_average(symbol, "25") > self.one_minutes_moving_average(symbol, "7"):
            # print(f"Buy/Long : {symbol}")
            self.buy_futures_contract(symbol)
            return symbol
        elif self.one_minutes_moving_average(symbol, "90") < self.one_minutes_moving_average(symbol, "25") < self.one_minutes_moving_average(symbol, "7"):
            # print(f"Sell/Short : {symbol}")
            # self.sell_futures_contract(symbol)
            self.sell_futures_contract(symbol)
            return symbol
        else:
            print(f"Asset {symbol} have no position for Buy/Sell")

    def one_minutes_buying_decision(self, symbol):
        if self.one_minutes_moving_average(symbol, "90") > self.one_minutes_moving_average(symbol, "25") > self.one_minutes_moving_average(symbol, "7"):
            print(f"Buy/Long : {symbol}")
            return "Long"
        elif self.one_minutes_moving_average(symbol, "90") < self.one_minutes_moving_average(symbol, "25") < self.one_minutes_moving_average(symbol, "7"):
            print(f"Sell/Short : {symbol}")
            return "Short"
        else:
            print(f"Asset {symbol} have no decision for Buy/Sell")


# OneMinuteMA().one_minutes_buying_decision("GALABUSD")
# print(OneMinuteMA().one_minutes_buying_decision("GALABUSD"))
# OneMinuteMA().one_minutes_moving_average(symbol="GALABUSD", look_back=90)

