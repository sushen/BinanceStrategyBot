import time

import pandas as pd

from all_variable import Variable
from api_callling.api_calling import APICall

from get_symbol.find_symbols import FindSymbols

from get_largest_pattern.get_pattern_in_data import GetPatternInData

from strategy.strategy import FinalStrategy

from get_largest_pattern.get_big_pattern import GetBiggerPattern

from strategy.searching_negative_base_on_today_positive_coin import SearchingNegativeSymbol

if __name__ == '__main__':
    findSymbol = FindSymbols()
    searching_negative = SearchingNegativeSymbol()
    findCandlePattern = GetPatternInData()
    final_strategy = FinalStrategy()
    get_bigger = GetBiggerPattern()
    for i in range(Variable.DAYS_YOU_RUN_THE_PROGRAM*24*60*60):
        print(f"\n-------------------------------{i + 1} time we searching for symbol-------------------------------\n")
        print(f"----------Find Last {Variable.STATIC_DAY} Days DATA----------")
        # if ((Variable.DAYS_YOU_RUN_THE_PROGRAM*24*60*60) % (24*60*60)) == 0:
        #     Variable.STATIC_DAY = 30
        time.sleep(5)
        ticker_info = pd.DataFrame(APICall.client.get_ticker())
        all_symbol = findSymbol.get_all_symbols('BUSD', ticker_info)
        negative_coins = searching_negative.negative_coin_search(all_symbol, Variable.STATIC_DAY)
        find_candle_set = findCandlePattern.keep_finding(negative_coins)
        symbol = get_bigger.get_bigger_pattern(find_candle_set)
        # symbol = ("IDEXBUSD")
        final_strategy.strategy_method(symbol)
