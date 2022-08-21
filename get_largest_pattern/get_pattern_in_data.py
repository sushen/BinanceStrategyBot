import time
from pprint import pprint

from dataframe.dataframe import GetDataframe

from main.all_variable import Variable

from get_largest_pattern.find_candle_pattern import FindCandlePattern


class GetPatternInData(FindCandlePattern, GetDataframe):

    clone_coins = []

    def find_and_return_pattern(self, pattern):
        for key, value in pattern.items():
            if value is not None:
                return pattern

    def fixed_negative_coins(self, negative_coins):
        if len(self.clone_coins) > 0:
            negative_coins = self.clone_coins
            self.clone_coins = []
            return negative_coins
        return negative_coins

    def find_candle_pattern(self, negative_coins, coin, candle_data):
        candle_pattern = self.candle_pattern(negative_coins, coin, candle_data)
        return candle_pattern

    def candle_pattern_dic(self, negative_coins, pattern_set):
        # TODO : We don need loop we will check one by one from list of cain
        for coin in negative_coins:

            candle_data = self.get_month_data(coin, 1, Variable.CANDLE_PATTERN_LOGBACK)
            candle_pattern = self.find_candle_pattern(negative_coins, coin, candle_data)

            pattern_set[coin] = candle_pattern
        print(pattern_set)
        return pattern_set

    print(clone_coins)
    print(input("Onside month :"))

    def get_pattern_in_one_month(self, negative_coins, pattern_with_set):
        negative_coins = self.fixed_negative_coins(negative_coins)
        return self.find_and_return_pattern(self.candle_pattern_dic(negative_coins, pattern_with_set))

    # print(input("Stop :"))

    def get_pattern_in_one_week(self, negative_coins, candle_pattern):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_week_data(coin, 1, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def get_pattern_in_three_days(self, negative_coins):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_day_data(coin, 3, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def get_pattern_in_one_days(self, negative_coins):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_month_data(coin, 1, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def get_pattern_in_twelve_hour(self, negative_coins):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_hour_data(coin, 12, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def get_pattern_in_eight_hour(self, negative_coins):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_hour_data(coin, 8, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def get_pattern_in_six_hour(self, negative_coins):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_hour_data(coin, 6, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def get_pattern_in_two_hour(self, negative_coins):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_hour_data(coin, 2, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def get_pattern_in_four_hour(self, negative_coins):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_hour_data(coin, 4, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def get_pattern_in_one_hour(self, negative_coins):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_hour_data(coin, 1, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def get_pattern_in_thirty_minute(self, negative_coins):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_minute_data(coin, 30, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def get_pattern_in_fifteen_minute(self, negative_coins):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_minute_data(coin, 15, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def get_pattern_in_five_minute(self, negative_coins):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_minute_data(coin, 5, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def get_pattern_in_three_minute(self, negative_coins):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_minute_data(coin, 3, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def get_pattern_in_one_minute(self, negative_coins):
        pattern_with_set = {}
        negative_coins = self.fixed_negative_coins(negative_coins)
        for coin in negative_coins:
            dataframe = GetDataframe()
            GetPatternInData.clone_coins.append(coin)
            candle_data = dataframe.get_minute_data(coin, 1, Variable.CANDLE_PATTERN_LOGBACK)
            cd_p = FindCandlePattern()
            candle_pattern = cd_p.candle_pattern(negative_coins, coin, candle_data)
            pattern_with_set[coin] = candle_pattern
        return self.find_and_return_pattern(pattern_with_set)

    def find_pattern_inside_various_time_frame(self, negative_coins, pattern_with_set):
        pattern_in_one_month = self.get_pattern_in_one_month(negative_coins, pattern_with_set)
        print(input("fixed Rest:"))
        pattern_in_one_week = self.get_pattern_in_one_week(negative_coins, pattern_with_set)
        pattern_in_three_days = self.get_pattern_in_three_days(negative_coins, pattern_with_set)
        pattern_in_one_days = self.get_pattern_in_one_days(negative_coins, pattern_with_set)
        pattern_in_twelve_hour = self.get_pattern_in_twelve_hour(negative_coins, pattern_with_set)
        pattern_in_eight_hour = self.get_pattern_in_eight_hour(negative_coins, pattern_with_set)
        pattern_in_six_hour = self.get_pattern_in_six_hour(negative_coins, pattern_with_set)
        pattern_in_four_hour = self.get_pattern_in_four_hour(negative_coins, pattern_with_set)
        pattern_in_two_hour = self.get_pattern_in_two_hour(negative_coins, pattern_with_set)
        pattern_in_one_hour = self.get_pattern_in_one_hour(negative_coins, pattern_with_set)
        pattern_in_thirty_minute = self.get_pattern_in_thirty_minute(negative_coins, pattern_with_set)
        pattern_in_fifteen_minute = self.get_pattern_in_fifteen_minute(negative_coins, pattern_with_set)
        pattern_in_five_minute = self.get_pattern_in_five_minute(negative_coins, pattern_with_set)
        pattern_in_three_minute = self.get_pattern_in_three_minute(negative_coins, pattern_with_set)
        pattern_in_one_minute = self.get_pattern_in_one_minute(negative_coins, pattern_with_set)

        if pattern_in_one_month is not None:
            print("inside one month")
            return pattern_in_one_month
        elif pattern_in_one_week is not None:
            print("inside one week")
            return pattern_in_one_week
        elif pattern_in_three_days is not None:
            print("inside three days")
            return pattern_in_three_days
        elif pattern_in_one_days is not None:
            print("inside one days")
            return pattern_in_one_days
        elif pattern_in_twelve_hour is not None:
            print("inside twelve hour")
            return pattern_in_twelve_hour
        elif pattern_in_eight_hour is not None:
            print("inside eight hour")
            return pattern_in_eight_hour
        elif pattern_in_six_hour is not None:
            print("inside six hour")
            return pattern_in_six_hour
        elif pattern_in_four_hour is not None:
            print("inside four hour")
            return pattern_in_four_hour
        elif pattern_in_two_hour is not None:
            print("inside two hour")
            return pattern_in_two_hour
        elif pattern_in_one_hour is not None:
            print("inside one hour")
            return pattern_in_one_hour
        elif pattern_in_thirty_minute is not None:
            print("inside thirty minute")
            return pattern_in_thirty_minute
        elif pattern_in_fifteen_minute is not None:
            print("inside fifteen minute")
            return pattern_in_fifteen_minute
        elif pattern_in_five_minute is not None:
            print("inside five minute")
            return pattern_in_five_minute
        elif pattern_in_three_minute is not None:
            print("inside three minute")
            return pattern_in_three_minute
        elif pattern_in_one_minute is not None:
            print("inside one minute")
            return pattern_in_one_minute

    def keep_finding(self, negative_coins, pattern_with_set):
        find_pattern_inside_various_time_frame = self.find_pattern_inside_various_time_frame(negative_coins, pattern_with_set)
        if find_pattern_inside_various_time_frame is not None:
            return find_pattern_inside_various_time_frame
        else:
            print("Empty pattern We have to run again\n")
            time.sleep(5)
            self.keep_finding(negative_coins)


ng_coins = ['LUNCBUSD', 'WRXBUSD']

# from get_symbol.find_symbols import FindSymbols
# from api_callling.api_calling import APICall
# import pandas as pd
# fs = FindSymbols()
# ticker_info = pd.DataFrame(APICall.client.get_ticker())
# all_symbol = fs.get_all_symbols("BUSD", ticker_info)
#
# from strategy.searching_negative_base_on_today_positive_coin import SearchingNegativeSymbol
# fk = SearchingNegativeSymbol()
# ng_coins = fk.negative_coin_search(all_symbol, Variable.SEARCHING_DAY)
# #
fcp = GetPatternInData()


# fcp.get_pattern_in_one_minute(ng_coins)
# fcp.get_pattern_in_five_minute(ng_coins)
# # time.sleep(61)
# fcp.find_pattern_inside_various_time_frame(ng_coins)
# print(fcp.get_pattern_in_one_month(ng_coins))
# fcp.keep_finding(ng_coins)
# tc = fcp.get_pattern_in_one_week(ng_coins)
pattern_with_set = {}
tc = fcp.keep_finding(ng_coins, pattern_with_set)
pprint(tc)
# fcp.find_pattern_inside_various_time_frame(ng_coins)
# if fcp.get_pattern_in_five_minute(ng_coins) is not None:
#     print("inside if")
#     print(fcp.get_pattern_in_five_minute(ng_coins))

# print(ng_coins)


