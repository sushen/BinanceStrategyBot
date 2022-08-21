from pprint import pprint

from api_callling.api_calling import APICall

from error_handleing.round import PriceRound


class Sell:

    def sell(self, currency, sell_currency_symbol):
        qty = PriceRound.round_selling_qty_price(self, currency)
        order = APICall.client.order_market_sell(
            symbol=sell_currency_symbol,
            quantity=qty,
        )

        pprint(order)
