"""
This class use for find negative coin .
When you call this method you need to pass all positive symbol as  argument.
"""

from dataframe.dataframe import GetDataframe
from main.all_variable import Variable


class SearchingNegativeSymbol:

    def negative_coin(self, all_symbol, searching_day):
        coins = []
        index = []
        all_symbols = [symbol for symbol in all_symbol['symbol']]

        print("\nSearching...\n")

        for symbol in all_symbols:
            index.append(len(all_symbols))
            # print(".")
            print(f"We are searching {searching_day} Days in  {str(len(index))}  no symbol named  {symbol}")

            day_data = GetDataframe().get_day_data(symbol, 1, searching_day)

            day_data_change_list = day_data['Change'].tolist()

            negative_coin_last_days = [value for value in day_data_change_list if
                                       value < 0 < day_data_change_list[-1]]

            if len(negative_coin_last_days) == (len(day_data_change_list) - 1):
                print(
                    f"\nWe find coin number {str(len(index))}  "
                    f"was negative {int(searching_day)} days,"
                    f"coin name: {symbol}\n")

                coins.append(day_data['symbol'][0])

        print(f"We find {len(coins)} coins are negative from yesterday\nCoin Names are:\n{coins}")
        return coins

    def zoom_coin_search(self, all_symbol, searching_day):

        coin_list = self.negative_coin(all_symbol, searching_day)

        for search in range(Variable.SEARCHING_DAY):
            search = search + 1
            running_day = Variable.SEARCHING_DAY - search
            print(f"Running Day : {running_day}")
            print(f"\nNumber of search : {search}")

            if running_day > 1:
                if len(coin_list) == 0:
                    print(f"\nDay of run: {running_day}")
                    coin_list = self.negative_coin(all_symbol, running_day)

                else:
                    # print("I am returning coin list")
                    return coin_list

    def negative_coin_search(self, all_symbol, searching_day):
        coin_list = self.zoom_coin_search(all_symbol, searching_day)

        if len(coin_list) == 0:
            coin_list = self.negative_coin_search(all_symbol, searching_day)
        else:
            return coin_list


# from get_symbol.find_symbols import FindSymbols
# from api_callling.api_calling import APICall
# import pandas as pd
#
# dataframe = GetDataframe()
# ticker_info = pd.DataFrame(APICall.client.get_ticker())
#
# fs = FindSymbols()
# all_symbol = fs.get_all_symbols("BUSD", ticker_info)
#
# fk = SearchingNegativeSymbol()
# print(fk.negative_coin_search(all_symbol, Variable.SEARCHING_DAY))

