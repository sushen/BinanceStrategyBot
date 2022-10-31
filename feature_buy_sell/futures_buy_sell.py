from api_callling.api_calling import APICall


class FuturesBuySell(APICall):
    def buy_futures_contract(self, symbol):
        sell = input("Type 'Yes' :")
        print(sell)
        if sell == "Yes":
            self.client.futures_create_order(symbol=symbol, side='BUY', type='MARKET', quantity=99)
            print(input("Done Buying :"))
        else:
            print("Technical indicator is not right")
        return symbol

    def sell_futures_contract(self, symbol):
        sell = input("Type 'Yes' :")
        print(sell)
        if sell == "Yes":
            self.client.futures_create_order(symbol=symbol, side='SELL', type='MARKET', quantity=99)
            print(input("Done Buying :"))
        else:
            print("Technical indicator is not right")
        return symbol
