import requests

class BC_data_ret:
    def __init__(self):
        pass

    def get_value(self, currency, amount):

        link = "https://blockchain.info/tobtc?currency={}&value={}".format(currency, amount)

        content = requests.get(link).content
        content = str(content, "utf-8")

        btc_price = float(amount)/float(content)
        print(content, btc_price)


bc = BC_data_ret()
bc.get_value("EUR", "1")