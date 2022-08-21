import time
from pprint import pprint

from main.all_variable import Variable

from api_callling.api_calling import APICall

from error_handleing.round import PriceRound

from email_option.sending_mail import MailSender


class Buy:
    order_buying_price = float(0)

    def coin_buy(self, currency_symbol):
        # print(input("_____:"))
        qty = PriceRound.round_symbol_price(self, currency_symbol)
        try:
            order = APICall.client.order_market_buy(
                symbol=currency_symbol,
                quantity=qty,
            )
        except:
            print("Exception IN ")
            time.sleep(2)
            qty = PriceRound.buy_error_round(self, currency_symbol)
            order = APICall.client.order_market_buy(
                symbol=currency_symbol,
                quantity=qty,
            )

        Buy.order_buying_price = float(order['fills'][0]['price'])
        receiver_mail = Variable.MAIL
        sender = MailSender()

        email_subject = f"We Buy {Buy.order_buying_price} coin"
        email_body = f"{order}"

        sender.send_mail(receiver_mail, email_subject, email_body)
        print(f'{email_subject}\n\n {email_body}')
        # pprint(order)





