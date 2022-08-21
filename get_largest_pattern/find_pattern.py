import talib


class FindPattern:

    def Hammer(self, candle_data):
        # Hammer
        candle_pattern = talib.CDLHAMMER(candle_data['Open'], candle_data['High'], candle_data['Low'],
                                         candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Belthold(self, candle_data):
        candle_pattern = talib.CDLBELTHOLD(candle_data['Open'], candle_data['High'], candle_data['Low'],
                                           candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Doji(self, candle_data):
        candle_pattern = talib.CDLDOJI(candle_data['Open'], candle_data['High'], candle_data['Low'],
                                       candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Three_Black_Crows(self, candle_data):
        candle_pattern = talib.CDL3BLACKCROWS(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Two_Crows(self, candle_data):
        candle_pattern = talib.CDL2CROWS(candle_data['Open'], candle_data['High'], candle_data['Low'],
                                         candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def ThreeInside(self, candle_data):
        candle_pattern = talib.CDL3INSIDE(candle_data['Open'], candle_data['High'], candle_data['Low'],
                                          candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def ThreeLineStrike(self, candle_data):
        candle_pattern = talib.CDL3LINESTRIKE(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def ThreeOutside(self, candle_data):
        candle_pattern = talib.CDL3OUTSIDE(candle_data['Open'], candle_data['High'], candle_data['Low'],
                                           candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def WhiteSoldiers(self, candle_data):
        candle_pattern = talib.CDL3WHITESOLDIERS(candle_data['Open'], candle_data['High'],
                                                 candle_data['Low'],
                                                 candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def DojiStar(self, candle_data):
        candle_pattern = talib.CDLDOJISTAR(candle_data['Open'], candle_data['High'], candle_data['Low'],
                                           candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def HangingMan(self, candle_data):
        candle_pattern = talib.CDLHANGINGMAN(candle_data['Open'], candle_data['High'],
                                             candle_data['Low'],
                                             candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def MorningStar(self, candle_data):
        candle_pattern = talib.CDLMORNINGSTAR(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def ShootingStar(self, candle_data):
        candle_pattern = talib.CDLSHOOTINGSTAR(candle_data['Open'], candle_data['High'],
                                               candle_data['Low'],
                                               candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:            return False

    def ThreeStarsinTheSouth(self, candle_data):
        candle_pattern = talib.CDL3STARSINSOUTH(candle_data['Open'], candle_data['High'],
                                                candle_data['Low'],
                                                candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Abandonedbaby(self, candle_data):
        candle_pattern = talib.CDLABANDONEDBABY(candle_data['Open'], candle_data['High'],
                                                candle_data['Low'],
                                                candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def AdvanceBlock(self, candle_data):
        candle_pattern = talib.CDLADVANCEBLOCK(candle_data['Open'], candle_data['High'],
                                               candle_data['Low'],
                                               candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Breakaway(self, candle_data):
        candle_pattern = talib.CDLBREAKAWAY(candle_data['Open'], candle_data['High'], candle_data['Low'],
                                            candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def closing_marubozu(self, candle_data):
        candle_pattern = talib.CDLCLOSINGMARUBOZU(candle_data['Open'], candle_data['High'],
                                                  candle_data['Low'],
                                                  candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def ConcealingBabySwallow(self, candle_data):
        candle_pattern = talib.CDLCONCEALBABYSWALL(candle_data['Open'], candle_data['High'],
                                                   candle_data['Low'],
                                                   candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False
    def Counterattack(self, candle_data):
        candle_pattern = talib.CDLCOUNTERATTACK(candle_data['Open'], candle_data['High'],
                                                candle_data['Low'],
                                                candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def DarkCloudCover(self, candle_data):
        candle_pattern = talib.CDLDARKCLOUDCOVER(candle_data['Open'], candle_data['High'],
                                                 candle_data['Low'],
                                                 candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Dragonfly_Doji(self, candle_data):
        candle_pattern = talib.CDLDRAGONFLYDOJI(candle_data['Open'], candle_data['High'],
                                                candle_data['Low'],
                                                candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Engulfing_Pattern(self, candle_data):
        candle_pattern = talib.CDLENGULFING(candle_data['Open'], candle_data['High'], candle_data['Low'],
                                            candle_data['Close'])
        process_data = candle_pattern[:-1]
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            for i in process_data:
                if i == 100:
                    return True
        else:
            return False

    def Evening_Star(self, candle_data):
        candle_pattern = talib.CDLEVENINGSTAR(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Gravestone_Doji(self, candle_data):
        candle_pattern = talib.CDLGRAVESTONEDOJI(candle_data['Open'], candle_data['High'],
                                                 candle_data['Low'],
                                                 candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Harami_Pattern(self, candle_data):
        candle_pattern = talib.CDLHARAMI(candle_data['Open'], candle_data['High'], candle_data['Low'],
                                         candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Harami_Cross_Pattern(self, candle_data):
        candle_pattern = talib.CDLHARAMICROSS(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Evening_Doji_Star(self, candle_data):
        candle_pattern = talib.CDLEVENINGDOJISTAR(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Up_Down_Gap_Side_White(self, candle_data):
        candle_pattern = talib.CDLGAPSIDESIDEWHITE(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def High_Wave_Candle(self, candle_data):
        candle_pattern = talib.CDLHIGHWAVE(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Hikkake(self, candle_data):
        candle_pattern = talib.CDLHIKKAKE(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Modified_Hikkake(self, candle_data):
        candle_pattern = talib.CDLHIKKAKEMOD(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Homing_Pigeon(self, candle_data):
        candle_pattern = talib.CDLHOMINGPIGEON(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Identical_Three_Crows(self, candle_data):
        candle_pattern = talib.CDLIDENTICAL3CROWS(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def In_Neck(self, candle_data):
        candle_pattern = talib.CDLINNECK(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Inverted_Hammer(self, candle_data):
        candle_pattern = talib.CDLINVERTEDHAMMER(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Kicking(self, candle_data):
        candle_pattern = talib.CDLKICKING(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Kicking_Determinded(self, candle_data):
        candle_pattern = talib.CDLKICKINGBYLENGTH(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Ladder_Bottom(self, candle_data):
        candle_pattern = talib.CDLLADDERBOTTOM(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Long_Legged_Doji(self, candle_data):
        candle_pattern = talib.CDLLONGLEGGEDDOJI(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Long_Line(self, candle_data):
        candle_pattern = talib.CDLLONGLINE(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Marubozu(self, candle_data):
        candle_pattern = talib.CDLMARUBOZU(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Matching_Low(self, candle_data):
        candle_pattern = talib.CDLMATCHINGLOW(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Mat_Hold(self, candle_data):
        candle_pattern = talib.CDLMATHOLD(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Morning_Doji_Star(self, candle_data):
        candle_pattern = talib.CDLMORNINGDOJISTAR(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def On_neck(self, candle_data):
        candle_pattern = talib.CDLONNECK(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Piercing(self, candle_data):
        candle_pattern = talib.CDLPIERCING(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False


    def Rickshaw_Man(self, candle_data):
        candle_pattern = talib.CDLRICKSHAWMAN(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False


    def Rising_Fall_3_Method(self, candle_data):
        candle_pattern = talib.CDLRISEFALL3METHODS(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Separating_Lines(self, candle_data):
        candle_pattern = talib.CDLSEPARATINGLINES(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Short_Line(self, candle_data):
        candle_pattern = talib.CDLSHORTLINE(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Spinning_Top(self, candle_data):
        candle_pattern = talib.CDLSPINNINGTOP(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Stalled(self, candle_data):
        candle_pattern = talib.CDLSTALLEDPATTERN(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Stick_Sandwich(self, candle_data):
        candle_pattern = talib.CDLSTICKSANDWICH(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Takuri(self, candle_data):
        candle_pattern = talib.CDLTAKURI(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Tasuri_Gap(self, candle_data):
        candle_pattern = talib.CDLTASUKIGAP(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Thrusting(self, candle_data):
        candle_pattern = talib.CDLTHRUSTING(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Tristar(self, candle_data):
        candle_pattern = talib.CDLTRISTAR(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Unique_3_River(self, candle_data):
        candle_pattern = talib.CDLUNIQUE3RIVER(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Upside_Gap_Two_Crows(self, candle_data):
        candle_pattern = talib.CDLUPSIDEGAP2CROWS(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False

    def Upside_Downside_Gap_Three_Methods(self, candle_data):
        candle_pattern = talib.stream_CDLXSIDEGAP3METHODS(candle_data['Open'], candle_data['High'],
                                              candle_data['Low'],
                                              candle_data['Close'])
        candle_data['candle_pattern'] = candle_pattern
        candle_pattern_count = candle_data[candle_data['candle_pattern'] != 0]
        # print(candle_pattern_count)
        # print(candle_pattern_count['candle_pattern'].values)
        if candle_pattern_count['candle_pattern'].size > 0:
            return True
        else:
            return False
