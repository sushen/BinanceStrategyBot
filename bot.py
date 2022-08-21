import json
import os
import time
from pprint import pprint
import talib
import asyncio
import pandas as pd
import websocket
from binance.client import Client
from binance import BinanceSocketManager

api_key = os.environ.get('binance_api_key')
api_secret = os.environ.get('binance_api_secret')


client = Client(api_key, api_secret)


day = '3'


def get_all_symbols():
    ticker_info = pd.DataFrame(client.get_ticker())
    # ticker_info = pd.DataFrame(client.get_all_tickers())
    busd_info = ticker_info[ticker_info.symbol.str.contains('BUSD')]
    # TODO : Try using .loc[row_indexer,col_indexer] = value instead
    # busd_info.set_index('priceChangePercent')
    # busd_info.priceChangePercent = pd.to_numeric(busd_info.priceChangePercent, errors='coerce')
    # print(f"{len(busd_info)} symbol we are processing.")
    non_leverage = busd_info[~(busd_info.symbol.str.contains('UP')) | (busd_info.symbol.str.contains('DOWN'))]
    # print(f"{len(non_leverage)} symbol we are processing.")
    non_leverage.priceChangePercent = non_leverage['priceChangePercent'].astype(float)
    non_leverage = non_leverage.sort_values(by='priceChangePercent', ascending=False)

    print(non_leverage)

    # print(input("Getting Top Symbol : "))
    non_leverage = non_leverage.iloc[:, :4]
    symbols = non_leverage.loc[non_leverage['priceChangePercent'].astype(float) > 0]
    # print(symbols)
    print(f"{len(symbols)} symbol we are processing.")
    # print(input("Getting Top Symbol : "))
    return symbols


def get_day_data(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + " day ago UTC"))
    frame = frame.iloc[:, :6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    change = ((frame['Close'] - frame['Open']) * 100) / frame['Open']
    frame['Change'] = change
    frame['symbol'] = symbol
    # print(frame)
    # print(input("Getting Day Data : "))
    return frame


index = []
coins = []
all_symbol = get_all_symbols()

# print(all_symbol['symbol'])


for symbol in all_symbol['symbol']:
    # print(input(" :"))
    index.append(len(all_symbol))
    print("We are searching in " + str(len(index)) + " no symbol named " + symbol)
    try:
        day_data = get_day_data(symbol, '1d', day)
    except:
        time.sleep(10)
        day_data = get_day_data(symbol, '1d', day)
    day_data_change_list = day_data['Change'].tolist()
    negative_coin_last_days = [value for value in day_data_change_list if value < 0 and day_data_change_list[-1] > 0]

    if len(negative_coin_last_days) == (len(day_data_change_list) - 1):
        print(f"\nWe find coin number {str(len(index))}  was negative {int(day) - 1} days, coin name: {symbol}\n")

        coins.append(day_data['symbol'][0])


def Hammer(candle_data_pera):
    # Hammer
    candle_pattern = talib.CDLHAMMER(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                     candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def Belthold(candle_data_pera):
    candle_pattern = talib.CDLBELTHOLD(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                       candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def Doji(candle_data_pera):
    candle_pattern = talib.CDLDOJI(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                   candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def Three_Black_Crows(candle_data_pera):
    candle_pattern = talib.CDL3BLACKCROWS(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                          candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def Two_Crows(candle_data_pera):
    candle_pattern = talib.CDL2CROWS(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                     candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def ThreeInside(candle_data_pera):
    candle_pattern = talib.CDL3INSIDE(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                      candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def ThreeLineStrike(candle_data_pera):
    candle_pattern = talib.CDL3LINESTRIKE(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                          candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def ThreeOutside(candle_data_pera):
    candle_pattern = talib.CDL3OUTSIDE(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                       candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def WhiteSoldiers(candle_data_pera):
    candle_pattern = talib.CDL3WHITESOLDIERS(candle_data_pera['Open'], candle_data_pera['High'],
                                             candle_data_pera['Low'],
                                             candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def DojiStar(candle_data_pera):
    candle_pattern = talib.CDLDOJISTAR(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                       candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def HangingMan(candle_data_pera):
    candle_pattern = talib.CDLHANGINGMAN(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                         candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def MorningStar(candle_data_pera):
    candle_pattern = talib.CDLMORNINGSTAR(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                          candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def ShootingStar(candle_data_pera):
    candle_pattern = talib.CDLSHOOTINGSTAR(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                           candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def ThreeStarsinTheSouth(candle_data_pera):
    candle_pattern = talib.CDL3STARSINSOUTH(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                            candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def Abandonedbaby(candle_data_pera):
    candle_pattern = talib.CDLABANDONEDBABY(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                            candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def AdvanceBlock(candle_data_pera):
    candle_pattern = talib.CDLADVANCEBLOCK(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                           candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def Breakaway(candle_data_pera):
    candle_pattern = talib.CDLBREAKAWAY(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                        candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def closing_marubozu(candle_data_pera):
    candle_pattern = talib.CDLCLOSINGMARUBOZU(candle_data_pera['Open'], candle_data_pera['High'],
                                              candle_data_pera['Low'],
                                              candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def ConcealingBabySwallow(candle_data_pera):
    candle_pattern = talib.CDLCONCEALBABYSWALL(candle_data_pera['Open'], candle_data_pera['High'],
                                               candle_data_pera['Low'],
                                               candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def Counterattack(candle_data_pera):
    candle_pattern = talib.CDLCOUNTERATTACK(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                            candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def DarkCloudCover(candle_data_pera):
    candle_pattern = talib.CDLDARKCLOUDCOVER(candle_data_pera['Open'], candle_data_pera['High'],
                                             candle_data_pera['Low'],
                                             candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def Dragonfly_Doji(candle_data_pera):
    candle_pattern = talib.CDLDRAGONFLYDOJI(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                            candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def Engulfing_Pattern(candle_data_pera):
    candle_pattern = talib.CDLENGULFING(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                        candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def Evening_Star(candle_data_pera):
    candle_pattern = talib.CDLEVENINGSTAR(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                          candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def Gravestone_Doji(candle_data_pera):
    candle_pattern = talib.CDLGRAVESTONEDOJI(candle_data_pera['Open'], candle_data_pera['High'],
                                             candle_data_pera['Low'],
                                             candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def Harami_Pattern(candle_data_pera):
    candle_pattern = talib.CDLHARAMI(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                     candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def Harami_Cross_Pattern(candle_data_pera):
    candle_pattern = talib.CDLHARAMICROSS(candle_data_pera['Open'], candle_data_pera['High'], candle_data_pera['Low'],
                                          candle_data_pera['Close'])
    candle_data_pera['candle_pattern'] = candle_pattern
    candle_pattern_count = candle_data_pera[candle_data_pera['candle_pattern'] != 0]
    # print(candle_pattern_count)
    # print(candle_pattern_count['candle_pattern'].values)
    if candle_pattern_count['candle_pattern'].size > 0:
        return True
    else:
        return False


def get_bigger_patten(dict):
    count = 0
    long_key = ""
    for key, value in dict.items():
        if len(value) > count:
            count = len(value)
            long_key = key
    print("Largest Pattern Key is : ", long_key)
    # TODO : we need to find more efficient way to find coin
    # TODO : We will grab more than one coin from here
    return long_key


# TODO : Play with compression work with 30m, 15m, 5m data
def get_hour_data(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + " hour ago UTC"))
    frame = frame.iloc[:, :6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    # print(frame)
    # print(input("Getting hourly Data : "))
    return frame


def find_candle_patterns(lockbacktime):
    # count = 0
    pattern_with_symbol = {}
    global positive_data
    positive_data = []

    for count, coin in enumerate(coins):
        # binance.exceptions.BinanceAPIException: APIError(code=-1100): Illegal characters found in parameter 'symbol'; legal range is '^[A-Z0-9-_.]{1,20}$'.
        candle_data = get_hour_data(coin, '1h', lockbacktime)
        candle_symbol = coins[count]
        coins[count] = []
        positive_data.append(candle_symbol)
        # print(input("..."))
        # TODO : Find Bullish and Bearish
        if Hammer(candle_data):
            coins[count].append("Hammer")
        if Belthold(candle_data):
            coins[count].append("Belthold")
        if Doji(candle_data):
            coins[count].append("Doji")
        if Three_Black_Crows(candle_data):
            coins[count].append("Three Black Crows")
        if Two_Crows(candle_data):
            coins[count].append("Two Crows")
        if ThreeInside(candle_data):
            coins[count].append("Three Inside")
        if ThreeOutside(candle_data):
            coins[count].append("Three Outside")
        if ThreeLineStrike(candle_data):
            coins[count].append("Three Line Strike")
        if WhiteSoldiers(candle_data):
            coins[count].append("White Soldiers")
        if DojiStar(candle_data):
            coins[count].append("Doji Star")
        if HangingMan(candle_data):
            coins[count].append("Hanging Man")
        if MorningStar(candle_data):
            coins[count].append("Morning Star")
        if ShootingStar(candle_data):
            coins[count].append("Shooting Star")
        if ThreeStarsinTheSouth(candle_data):
            coins[count].append("Three Stars in The South")
        if Abandonedbaby(candle_data):
            coins[count].append("Abandoned baby")
        if AdvanceBlock(candle_data):
            coins[count].append("Advance Block")
        if Breakaway(candle_data):
            coins[count].append("Break Away")
        if closing_marubozu(candle_data):
            coins[count].append("Closing Marubozu")
        if ConcealingBabySwallow(candle_data):
            coins[count].append("Concealing Baby Swallow")
        if Counterattack(candle_data):
            coins[count].append("Counter attack")
        if DarkCloudCover(candle_data):
            coins[count].append("Dark Cloud Cover")
        if Evening_Star(candle_data):
            coins[count].append("Evening_Star")
        if Dragonfly_Doji(candle_data):
            coins[count].append("Dragonfly Doji")
        if Engulfing_Pattern(candle_data):
            coins[count].append("Engulfing Pattern")
        if Gravestone_Doji(candle_data):
            coins[count].append("Gravestone Doji")
        if Harami_Pattern(candle_data):
            coins[count].append("Harami Pattern")
        if Harami_Cross_Pattern(candle_data):
            coins[count].append("Harami Cross Pattern")
        print(f"{candle_symbol} have {len(coins[count])} pattern which is  {coins[count]} ")
        pattern_with_symbol[candle_symbol] = coins[count]
    return get_bigger_patten(pattern_with_symbol)


append_currency = []


def on_message(ws, message):
    json_message = json.loads(message)
    current_data = json_message["k"]["c"]
    append_currency.append(current_data)
    ws.close()


def on_error(ws, error):
    print(error)


def on_close(close_msg):
    print("### closed ###" + close_msg)


def streamKline(currency, interval):
    websocket.enableTrace(False)
    socket = f'wss://stream.binance.com:9443/ws/{currency}@kline_{interval}'
    ws = websocket.WebSocketApp(socket,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()
"""
৪ - খুজে পেলে সেই কয়েন টা কিনবো
"""

# We already find way to get symbol
# TODO : Why we searching this on 30 hourly candle
# We Define This base on our balance
buying_dollar = 11
# We will find it base on support and resistance
stop_loss_limit = 0.05
# We Can define it base on coin history how much percentage we increasing
change_stop_loss_when_buying_price_change = .25
# There will be more change on second stop loss, and we will find third and forth one also
second_stop_loss = 2

interval = '1m'


def round_symbol_price(currency_symbol):
    avg_price = client.get_avg_price(symbol=currency_symbol)
    amount_of_usd = buying_dollar
    round_with_usd = float(amount_of_usd) / float(avg_price['price'])
    # print(input("--"))
    if round_with_usd >= 10:
        dollar_convert = round(round_with_usd)
        print(f"{dollar_convert} is bigger than 10")
    elif round_with_usd >= 1:
        dollar_convert = round(round_with_usd, 2)
        print(f"{dollar_convert} is bigger than 1")
    elif round_with_usd < 0.6:
        dollar_convert = round(round_with_usd, 2)
        print(f"{dollar_convert} is smaller than 0.6")
    elif round_with_usd < 1:
        dollar_convert = round(round_with_usd, 4)
        print(f"{dollar_convert} is smaller than 1")
    elif round_with_usd < .005:
        dollar_convert = round(round_with_usd, 5)
        print(f"{dollar_convert} is smaller than 0.005")
    return dollar_convert


def round_qty_price(currency):
    if currency >= 10:
        dollar_convert = int(currency)
    elif currency >= 1:
        str_currency = str(currency)
        currency = str_currency[:4]
        dollar_convert = float(currency)
    elif currency < 1:
        str_currency = str(currency)
        currency = str_currency[:6]
        dollar_convert = float(currency)
    elif currency < .005:
        dollar_convert = round(currency, 5)
    print(f"{dollar_convert} is final")
    return dollar_convert


def get_minute_data(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + " min ago UTC"))
    frame = frame.iloc[:, :6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    # print(frame)
    return frame


def strategy(lookback_hours="15",  stop_loss=.015, entried=False):
    largest_symbol = find_candle_patterns(lookback_hours)
    qty = round_symbol_price(largest_symbol)
    print(qty)
    if not entried:
        order = client.order_market_buy(
            symbol=largest_symbol,
            quantity=qty,
        )
        pprint(order)
        entried = True

    if entried:
        while True:
            symbol_balance = client.get_asset_balance(asset=largest_symbol[:-4])
            time.sleep(1)
            while symbol_balance is not None:
                time.sleep(1)
                highest_price = []
                buying_price = float(order['fills'][0]['price'])

                while True:
                    streamKline(largest_symbol.lower(), interval)
                    time.sleep(1)
                    symbol_sell_balance = client.get_asset_balance(asset=largest_symbol[:-4])
                    print(symbol_sell_balance)
                    currency = float(symbol_sell_balance['free'])
                    # try:
                    #     avg_price = client.get_avg_price(symbol=symbol)
                    # except:
                    #     time.sleep(31)
                    #     avg_price = client.get_avg_price(symbol=symbol)

                    current_price = float(append_currency[-1])

                    sell_qty = round_qty_price(currency)

                    if len(highest_price) == 0:
                        highest_price.append(current_price)

                    if current_price > highest_price[-1]:
                        highest_price.append(current_price)

                    current_profit = float(current_price) - float(highest_price[-1])
                    print(f"{current_profit} : current profit")
                    sell_now_profit = float(current_price) - float(buying_price)
                    print(f"{sell_now_profit} : Sell Now Profit")

                    print(f"{current_price} : current price")
                    print(f"{buying_price} : buying price")
                    print(f"{highest_price[-1]} : highest price")
                    print(f"{highest_price[-1] - (highest_price[-1] * stop_loss)} : Stop-loss selling price\n")

                    if current_price < (highest_price[-1] - (highest_price[-1] * stop_loss)):
                        profit = (highest_price[-1] - (highest_price[-1] * stop_loss)) - buying_price
                        print(f"{profit} : Total profit")
                        print("sell")
                        order = client.order_market_sell(
                            symbol=largest_symbol,
                            quantity=sell_qty,
                        )

                        pprint(order)
                        break


                break
            break


for i in range(7 * 24 * 60 * 60):
    print(f"\n------------------{i+1} time we searching for symbol-------------------\n")
    time.sleep(5)
    strategy(stop_loss=0.015)
    coins = positive_data