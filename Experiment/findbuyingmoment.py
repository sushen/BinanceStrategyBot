from Experiment.experiment import CloneFindCandlePattern
# from dataframe.dataframe import GetDataframe
#
# from get_symbol.searching_negative_coin import SearchingNegetiveSymbol
#
# from experiment2 import GetBiggerPattern
# from main.all_variable import Variable


class FindBuyingMoment:

    def hello_test(self):
        print("hello")

    # Minutes = [1, 3, 5, 15, 30]
    # Hours = [1, 3, 5, 10, 15, 20]
    # Days = [1, 2, 3, 4, 5]
    # Num = 1
    # Interval = 0
    # Dataframe_Change = 0
    #
    # def __init__(self, coin, logback):
    #     self.coin = coin
    #     self.logback = logback
    #
    # def condition(self):
    #     SearchingNegetiveSymbol.index = []
    #     SearchingNegetiveSymbol.coins = []
    #     SearchingNegetiveSymbol.negative_coin(self)
    #     if FindBuyingMoment.Dataframe_Change == 0:
    #         if FindBuyingMoment.Num > len(FindBuyingMoment.Days):
    #             FindBuyingMoment.Dataframe_Change = 1
    #             FindBuyingMoment.Num = 1
    #         else:
    #             FindBuyingMoment.Interval = FindBuyingMoment.Days[len(FindBuyingMoment.Days) - FindBuyingMoment.Num]
    #             FindBuyingMoment.Num = FindBuyingMoment.Num + 1
    #             all_pattern_set = CloneFindCandlePattern.find_candle_pattern_func(self)
    #             return GetBiggerPattern.get_bigger_pattern(all_pattern_set)
    #     elif FindBuyingMoment.Dataframe_Change == 1:
    #         if FindBuyingMoment.Num > len(FindBuyingMoment.Hours):
    #             FindBuyingMoment.Dataframe_Change = 2
    #             FindBuyingMoment.Num = 1
    #         else:
    #             FindBuyingMoment.Interval = FindBuyingMoment.Hours[len(FindBuyingMoment.Hours) - FindBuyingMoment.Num]
    #             FindBuyingMoment.Num = FindBuyingMoment.Num + 1
    #             all_pattern_set = CloneFindCandlePattern.find_candle_pattern_func(self)
    #             return GetBiggerPattern.get_bigger_pattern(all_pattern_set)
    #     elif FindBuyingMoment.Dataframe_Change == 2:
    #         if FindBuyingMoment.Num > len(FindBuyingMoment.Minutes):
    #             FindBuyingMoment.Num = 1
    #             GetBiggerPattern.Going_Condition = 0
    #
    #         else:
    #             FindBuyingMoment.Interval = FindBuyingMoment.Minutes[len(FindBuyingMoment.Minutes) - FindBuyingMoment.Num]
    #             FindBuyingMoment.Num = FindBuyingMoment.Num + 1
    #             all_pattern_set = CloneFindCandlePattern.find_candle_pattern_func(self)
    #             return GetBiggerPattern.get_bigger_pattern(all_pattern_set)
    #
    # def pattern_dataframe(self):
    #     dataframe = GetDataframe(self.coin, self.Interval, self.logback)
    #     if FindBuyingMoment.Dataframe_Change == 0:
    #         print(f"----------Find Last {Variable.DAYS_TO_FIND_DATA} Days DATAS {FindBuyingMoment.Interval} "
    #               f"Days Pattern----------")
    #         return dataframe.get_day_data()
    #     elif FindBuyingMoment.Dataframe_Change == 1:
    #         print(f"----------Find Last {Variable.DAYS_TO_FIND_DATA} Days DATAS {FindBuyingMoment.Interval} "
    #               f"Hours Pattern----------")
    #         return dataframe.get_hour_data()
    #     else:
    #         print(f"----------Find Last {Variable.DAYS_TO_FIND_DATA} Days DATAS {FindBuyingMoment.Interval} "
    #               f"Minutes Pattern----------")
    #         return dataframe.get_minute_data()


test_hello = FindBuyingMoment()
test_hello.hello_test()


