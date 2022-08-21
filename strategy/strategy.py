import time

from buy.buy import Buy

from sell.selling_strategy import SellingStrategy

from buy.buying_strategy import BuyingStrategy

from api_callling.api_calling import APICall


class FinalStrategy:
    def strategy_method(self, symbol, entries=False):
        currency_symbol = symbol
        symbol_balance = APICall.client.get_asset_balance(asset=currency_symbol[:-4])
        if not entries:
            buy_method = BuyingStrategy(currency_symbol)
            buy_method.buying_condition()
            entries = True

        if entries:
            while True:
                symbol_balance = symbol_balance
                time.sleep(1)
                while symbol_balance is not None:
                    time.sleep(1)
                    buying_price_para = Buy.order_buying_price
                    sell_method = SellingStrategy(currency_symbol, buying_price_para)
                    sell_method.selling_condition()
                    break
                break


# fs = FinalStrategy()
# fs.strategy_method("BTCBUSD")
