import time

from moving_average.one_minute_moving_average import OneMinuteMA
from moving_average.three_minute_moving_average import ThreeMinuteMA


# class Decision(OneMinuteMA, ThreeMinuteMA):
#     def one_minute_decision(self, symbol):
#         if self.one_minutes_buying_decision(symbol) is not None:
#             print("One Minute Decision Running ... ")
#             return self.one_minutes_buying_decision(symbol)
#         else:
#             return "No Signal"
#
#     def three_minute_decision(self, symbol):
#         if self.three_minute_decision(symbol) is not None:
#             print("Three Minute Decision Running ... ")
#             return self.three_minute_decision(symbol)
#         else:
#             return "No Signal"
#
#     def decision(self, symbol):
#         if len(self.one_minute_decision(symbol)) > 5:
#             print(len(self.one_minute_decision(symbol)))
#             one_mints_symbol = [symbol]
#             print(one_mints_symbol)
#             print(input("Stop :"))
#             if len(self.three_minute_decision(symbol)) > 5:
#                 print(symbol)
#
#         if len(self.three_minute_decision(symbol)) > 5:
#             print(symbol)
#         else:
#             print("No")


# Decision().decision("FTMBUSD")
#
import pandas as pd
from api_callling.api_calling import APICall

from get_symbol.find_symbols import FindSymbols

fs = FindSymbols()
# decision = Decision()

futures_exchange_info = APICall.client.futures_exchange_info()
trading_pairs = [info['symbol'] for info in futures_exchange_info['symbols']]


def feature_coin_buying_signal():
    ticker_info = pd.DataFrame(APICall.client.get_ticker())
    all_symbol = fs.get_all_symbols("BUSD", ticker_info)
    for symbol in all_symbol["symbol"]:
        string = symbol
        print(f"We are passing the {symbol} for decision.\n")
        result = [word for word in trading_pairs if word in string]

        if len(result) != 0:
            one_minutes_decision = OneMinuteMA().one_minutes_buying_decision(symbol)

            if one_minutes_decision == "Short":
                print("Decide Position Base On One Minutes\n")
                print(input(f"Short {symbol} :"))

                three_minutes_decision = ThreeMinuteMA().three_minutes_buying_decision(symbol)
                if three_minutes_decision == "Short":
                    print("Decide Position Base On Three Minutes")

            elif one_minutes_decision == "Long":
                print("Decide Position Base On One Minutes\n")
                print(input(f"Long {symbol} :"))

                three_minutes_decision = ThreeMinuteMA().three_minutes_buying_decision(symbol)
                if three_minutes_decision == "Long":
                    print("Decide Position Base On Three Minutes")

            # print(input("Stop :"))
            # decision.three_minute_decision(symbol)

    # print(input("stop :"))


feature_coin_buying_signal()
