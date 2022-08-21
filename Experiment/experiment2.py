from main.all_variable import Variable

from Experiment.experiment import CloneFindCandlePattern

from strategy.searching_negative_base_on_today_positive_coin import SearchingNegetiveSymbol

from experiment import FindBuyingMoment


class GetBiggerPattern:

    Going_Condition = 1

    def get_bigger_pattern(self, dictionary):
        count = 0
        long_key = ""
        for key, value in dictionary.items():
            if len(value) > count:
                count = len(value)
                long_key = key
        long_key = self.empty_key_error_handeling(long_key)
        print("Largest Pattern Key is: ", long_key)
        # TODO: We need to find Logical Error
        return long_key

    def empty_key_error_handeling(self, long_key_error):
        if long_key_error == "":
            print("______Empty Pattern, Please wait for 1 Minute .... (Happy Trading)_______")
            if self.Going_Condition == 1:
                CloneFindCandlePattern.Interval_Start = 1
                FindBuyingMoment.condition(self)
            Variable.STATIC_DAY = Variable.STATIC_DAY - 1
            if Variable.STATIC_DAY == 1:
                Variable.STATIC_DAY = Variable.CONDITION_STATIC_DAY
            Variable.DAYS_TO_FIND_DATA = str(Variable.STATIC_DAY)
            print(f"----------Find Last {Variable.DAYS_TO_FIND_DATA} Days DATA----------")
            SearchingNegetiveSymbol.index = []
            SearchingNegetiveSymbol.coins = []
            SearchingNegetiveSymbol.negative_coin(self)
            all_pattern_set = CloneFindCandlePattern.find_candle_pattern_func(self)
            return self.get_bigger_pattern(all_pattern_set)
        else:
            return long_key_error
