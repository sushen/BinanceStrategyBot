"""
This class use for find negative coin .
When you call this method you need to pass all positive symbol as  argument.
"""

import pandas as pd

from dataframe.dataframe import GetDataframe
from email_option.sending_mail import MailSender

from main.all_variable import Variable

class SearchingNegativeSymbol:
    DAYS_TO_FIND_DATA = str(Variable.STATIC_DAY)
    NEGATIVE_COINS = ''

    def negative_coin(self, all_symbols):
        coins = []
        index = []

        for symbol in all_symbols:
            index.append(len(all_symbols))
            print(f"We are searching in {str(len(index))} no symbol named {symbol} of last {SearchingNegativeSymbol.DAYS_TO_FIND_DATA} Days")
            day_data = GetDataframe().get_day_data(symbol, 1, SearchingNegativeSymbol.DAYS_TO_FIND_DATA)
            day_data_change_list = day_data['Change'].tolist()
            negative_coin_last_days = [value for value in day_data_change_list if
                                           value < 0 and day_data_change_list[-1] > 0]
            if len(negative_coin_last_days) == (len(day_data_change_list) - 1):
                print(
                    f"\nWe find coin number {str(len(index))}  "
                    f"was negative {int(SearchingNegativeSymbol.DAYS_TO_FIND_DATA) - 1} days,"
                    f"coin name: {symbol}\n")

                coins.append(day_data['symbol'][0])

        print(f"We find {len(coins)} coins are negative from yesterday\nCoin Names are:\n{coins}")
        return coins

    # TODO : Makes Day change Function and Add Here

    def zoom_condition(self):
        condition_static_day = Variable.STATIC_DAY
        Variable.STATIC_DAY = Variable.STATIC_DAY - 1
        SearchingNegativeSymbol.DAYS_TO_FIND_DATA = str(Variable.STATIC_DAY)
        SearchingNegativeSymbol.NEGATIVE_COINS = ""

    def check_condition(self, all_symbol):
        all_symbols = [symbol for symbol in all_symbol['symbol']]
        negative_coin = self.negative_coin(all_symbols)
        if len(negative_coin) > 0:
            SearchingNegativeSymbol.NEGATIVE_COINS = negative_coin
            return negative_coin
        else:
            self.zoom_condition()
            self.check_condition(all_symbol)

    def day_zoom(self, all_symbol):
        self.check_condition(all_symbol)
        return SearchingNegativeSymbol.NEGATIVE_COINS



# from get_symbol.find_symbols import FindSymbols
# from api_callling.api_calling import APICall
# ticker_info = pd.DataFrame(APICall.client.get_ticker())
#
# fs = FindSymbols()
# all_symbol = fs.get_all_symbols("BUSD", ticker_info)
#
# fk = SearchingNegativeSymbol()
# t = fk.day_zoom(all_symbol)
# # t = fk.check(all_symbol)
# print(t)
