class GetBiggerPattern:

    # def empty_key_error_handeling(self, long_key_error):
    #     if long_key_error == "":
    #         print("______Empty Pattern, Please wait for 1 Minute .... (Happy Trading)_______")
    #         Variable.STATIC_DAY = Variable.STATIC_DAY - 1
    #         if Variable.STATIC_DAY == 1:
    #             Variable.STATIC_DAY = Variable.CONDITION_STATIC_DAY
    #         Variable.DAYS_TO_FIND_DATA = str(Variable.STATIC_DAY)
    #         print(f"----------Find Last {Variable.DAYS_TO_FIND_DATA} Days DATA----------")
    #
    #
    #         fs = FindSymbols()
    #         all_symbol = fs.get_all_symbols("BUSD")
    #
    #
    #         negative_coin = SearchingNegativeSymbol.negative_coin(self, all_symbol)
    #         print(negative_coin)
    #         all_pattern_set = GetPatternInData.get_pattern_in_one_minute(negative_coin)
    #
    #         return self.get_bigger_pattern(all_pattern_set)
    #     else:
    #         return long_key_error

    def get_bigger_pattern(self, dictionary):
        count = 0
        long_key = ""
        for key, value in dictionary.items():
            if value is None:
                continue
            else:
                if len(value) > count:
                    count = len(value)
                    long_key = key
        # long_key = self.empty_key_error_handeling(long_key)
        print("Largest Pattern Key is: ", long_key)
        # TODO: We need to find Logical Error
        return long_key


# pattern_dictionary = {'GRTBUSD': None, 'JOEBUSD': [], 'CTXCBUSD': [], 'ENSBUSD': [], 'CVXBUSD': [], 'IMXBUSD': [], 'ATABUSD': [], 'MASKBUSD': [], 'ETHBUSD': [], 'AVAXBUSD': [], 'ALGOBUSD': [], 'CELRBUSD': [], 'ROSEBUSD': [], '1INCHBUSD': [], 'IOTXBUSD': [], 'BALBUSD': [], 'COMPBUSD': [], 'RNDRBUSD': [], 'MKRBUSD': [], 'HNTBUSD': [], 'C98BUSD': [], 'GALABUSD': ['Engulfing Pattern'], 'FLUXBUSD': [], 'CKBUSDT': [], 'SFPBUSD': [], 'FTMBUSD': [], 'ARBUSD': ['Engulfing Pattern', 'Engulfing Pattern'], 'REQBUSD': []}

# from get_symbol.find_symbols import FindSymbols
# fs = FindSymbols()
# all_symbol = fs.get_all_symbols("BUSD")
#
# fk = SearchingNegativeSymbol()
# ng_coins = fk.negative_coin_search(all_symbol)
#
# pattern_dictionary = GetPatternInData().keep_finding(ng_coins)


# gpd = GetPatternInData()
# pattern_dictionary = gpd.keep_finding(ng)
# gbp = GetBiggerPattern()
# large_coin = gbp.get_bigger_pattern(pattern_dictionary)
# print(large_coin)
