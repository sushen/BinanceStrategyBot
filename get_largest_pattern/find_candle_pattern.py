from get_largest_pattern.find_pattern import FindPattern


class FindCandlePattern:

    def candle_pattern(self, negative_coins, candle_symbol, candle_data):
        count = 0

        negative_coins[count] = []

        if candle_data is not None:
            if FindPattern.Hammer(self, candle_data):
                negative_coins[count].append("Hammer")
            if FindPattern.Belthold(self, candle_data):
                negative_coins[count].append("Belthold")
            if FindPattern.Doji(self, candle_data):
                negative_coins[count].append("Doji")
            if FindPattern.Three_Black_Crows(self, candle_data):
                negative_coins[count].append("Three Black Crows")
            if FindPattern.Two_Crows(self, candle_data):
                negative_coins[count].append("Two Crows")
            if FindPattern.ThreeInside(self, candle_data):
                negative_coins[count].append("Three Inside")
            if FindPattern.ThreeOutside(self, candle_data):
                negative_coins[count].append("Three Outside")
            if FindPattern.ThreeLineStrike(self, candle_data):
                negative_coins[count].append("Three Line Strike")
            if FindPattern.WhiteSoldiers(self, candle_data):
                negative_coins[count].append("White Soldiers")
            if FindPattern.DojiStar(self, candle_data):
                negative_coins[count].append("Doji Star")
            if FindPattern.HangingMan(self, candle_data):
                negative_coins[count].append("Hanging Man")
            if FindPattern.MorningStar(self, candle_data):
                negative_coins[count].append("Morning Star")
            if FindPattern.ShootingStar(self, candle_data):
                negative_coins[count].append("Shooting Star")
            if FindPattern.ThreeStarsinTheSouth(self, candle_data):
                negative_coins[count].append("Three Stars in The South")
            if FindPattern.Abandonedbaby(self, candle_data):
                negative_coins[count].append("Abandoned baby")
            if FindPattern.AdvanceBlock(self, candle_data):
                negative_coins[count].append("Advance Block")
            if FindPattern.Breakaway(self, candle_data):
                negative_coins[count].append("Break Away")
            if FindPattern.closing_marubozu(self, candle_data):
                negative_coins[count].append("Closing Marubozu")
            if FindPattern.ConcealingBabySwallow(self, candle_data):
                negative_coins[count].append("Concealing Baby Swallow")
            if FindPattern.Counterattack(self, candle_data):
                negative_coins[count].append("Counter attack")
            if FindPattern.DarkCloudCover(self, candle_data):
                negative_coins[count].append("Dark Cloud Cover")
            if FindPattern.Evening_Star(self, candle_data):
                negative_coins[count].append("Evening_Star")
            if FindPattern.Dragonfly_Doji(self, candle_data):
                negative_coins[count].append("Dragonfly Doji")
            if FindPattern.Engulfing_Pattern(self, candle_data):
                # engulfing = EngulfingPattern.engulfing_pattern_condtion(self, candle_data)
                negative_coins[count].append("Engulfing Pattern")
            if FindPattern.Gravestone_Doji(self, candle_data):
                negative_coins[count].append("Gravestone Doji")
            if FindPattern.Harami_Pattern(self, candle_data):
                negative_coins[count].append("Harami Pattern")
            if FindPattern.Harami_Cross_Pattern(self, candle_data):
                negative_coins[count].append("Harami Cross Pattern")
            if FindPattern.Evening_Doji_Star(self, candle_data):
                negative_coins[count].append("Evening Doji Star Pattern")
            if FindPattern.Up_Down_Gap_Side_White(self, candle_data):
                negative_coins[count].append("Up Down Gap Side White")
            if FindPattern.High_Wave_Candle(self, candle_data):
                negative_coins[count].append("High-Wave Candle")
            if FindPattern.Hikkake(self, candle_data):
                negative_coins[count].append("Hikkake Pattern")
            if FindPattern.Modified_Hikkake(self, candle_data):
                negative_coins[count].append("Modified Hikkake Pattern")
            if FindPattern.Homing_Pigeon(self, candle_data):
                negative_coins[count].append("Homing Pigeon Pattern")
            if FindPattern.Identical_Three_Crows(self, candle_data):
                negative_coins[count].append("Identical Three Crows Pattern")
            if FindPattern.In_Neck(self, candle_data):
                negative_coins[count].append("In-Neck Pattern")
            if FindPattern.Inverted_Hammer(self, candle_data):
                negative_coins[count].append("Inverted Hammer Pattern")
            if FindPattern.Kicking(self, candle_data):
                negative_coins[count].append("Kicking Pattern")
            if FindPattern.Kicking_Determinded(self, candle_data):
                negative_coins[count].append("Kicking - bull/bear determined by the longer marubozu Pattern")
            if FindPattern.Ladder_Bottom(self, candle_data):
                negative_coins[count].append("Ladder Bottom Pattern")
            if FindPattern.Long_Legged_Doji(self, candle_data):
                negative_coins[count].append("Long Legged Doji Pattern")
            if FindPattern.Long_Line(self, candle_data):
                negative_coins[count].append("Long Line Candle Pattern")
            if FindPattern.Marubozu(self, candle_data):
                negative_coins[count].append("Marubozu Pattern")
            if FindPattern.Matching_Low(self, candle_data):
                negative_coins[count].append("Matching Low Pattern")
            if FindPattern.Mat_Hold(self, candle_data):
                negative_coins[count].append("Mat Hold Pattern")
            if FindPattern.Morning_Doji_Star(self, candle_data):
                negative_coins[count].append("Morning Doji Star Pattern")
            if FindPattern.On_neck(self, candle_data):
                negative_coins[count].append("On-Neck Pattern")
            if FindPattern.Piercing(self, candle_data):
                negative_coins[count].append("Piercing Pattern")
            if FindPattern.Rickshaw_Man(self, candle_data):
                negative_coins[count].append("Rickshaw Man Pattern")
            if FindPattern.Rising_Fall_3_Method(self, candle_data):
                negative_coins[count].append("Rising/Falling Three Methods")
            if FindPattern.Separating_Lines(self, candle_data):
                negative_coins[count].append("Separating Lines Pattern")
            if FindPattern.Short_Line(self, candle_data):
                negative_coins[count].append("Short Line Candle")
            if FindPattern.Spinning_Top(self, candle_data):
                negative_coins[count].append("Spinning Top Pattern")
            if FindPattern.Stalled(self, candle_data):
                negative_coins[count].append("Stalled  Pattern")
            if FindPattern.Stick_Sandwich(self, candle_data):
                negative_coins[count].append("Stick Sandwich Pattern")
            if FindPattern.Takuri(self, candle_data):
                negative_coins[count].append("Takuri (Dragonfly Doji with very long lower shadow) Pattern")
            if FindPattern.Tasuri_Gap(self, candle_data):
                negative_coins[count].append("Tasuki Gap Pattern")
            if FindPattern.Thrusting(self, candle_data):
                negative_coins[count].append("Thrusting Pattern")
            if FindPattern.Tristar(self, candle_data):
                negative_coins[count].append("Tristar Pattern")
            if FindPattern.Unique_3_River(self, candle_data):
                negative_coins[count].append("Unique 3 River Pattern")
            if FindPattern.Upside_Gap_Two_Crows(self, candle_data):
                negative_coins[count].append("Upside Gap Two Crows Pattern")
            if FindPattern.Upside_Downside_Gap_Three_Methods(self, candle_data):
                negative_coins[count].append("Upside/Downside Gap Three Methods")
        # if len(negative_coins[count]) > 0:
        pattern_each_set_value = negative_coins[count]

        if len(pattern_each_set_value) > 0:
            print(f"{candle_symbol} have {len(negative_coins[count])} pattern which is  "
                  f"{negative_coins[count]} ")
            return pattern_each_set_value
        else:
            print(f"{candle_symbol} have {len(negative_coins[count])} pattern")
            return None


# nc = ['BTCBUSD', 'LUNABUSD', 'AMPBUSD', 'ASRBUSD']
# from dataframe.dataframe import GetDataframe
# minute_dataframe = GetDataframe()
# for i in nc:
#     candle_data = minute_dataframe.get_minute_data(i, '1', "11")
#     cd_p = FindCandlePattern()
#     print(cd_p.candle_pattern(nc, i, candle_data))