using_dict = {'DENTBUSD': [], 'AUDBUSD': ['Hammer', 'Belthold', 'Doji', 'Hanging Man', 'Closing Marubozu', 'Dragonfly Doji', 'Up Down Gap Side White', 'Long Legged Doji Pattern', 'Long Line Candle Pattern', 'Marubozu Pattern', 'Matching Low Pattern', 'Short Line Candle', 'Takuri (Dragonfly Doji with very long lower shadow) Pattern'], 'USDCBUSD': ['Belthold', 'Doji', 'Closing Marubozu', 'Gravestone Doji', 'Long Legged Doji Pattern', 'Long Line Candle Pattern', 'Marubozu Pattern', 'Short Line Candle']}

count = 0


def condition(pattern_set):
    for key, value in pattern_set.items():
        if len(value) > count:
            print("You Have Pattern")
            print((f"Pattern: {pattern_set}"))
            return pattern_set
        else:
            print("No Data Here ")
            break



condition(using_dict)
