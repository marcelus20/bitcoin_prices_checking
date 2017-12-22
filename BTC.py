import requests

#THIS FUNCTION WILL SEND AN HTTPREQUEST TO THE LINK BELOW AND GET THE CONTENT
def get_value(currency, amount):
    link = "https://blockchain.info/tobtc?currency={}&value={}".format(currency, amount)

    #CONTENT IS A REQUEST TO THAT LINK
    content = requests.get(link).content
    #CONVERTING TO A STRING
    content = str(content, "utf-8")

    #GETTING THE BTC VALUE FORMULA
    btc_price = float(amount) / float(content)
    return "{:^.2f}".format(btc_price)