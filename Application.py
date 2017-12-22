import requests
from matplotlib import pyplot

from BTC import get_value
import datetime
import time

"""
THIS APLICATION WILL RETRIEVE DATA FROM THE NETWORK AND WRITE THE RESULTS DOWN TO A FILE
IT GETS THE BITCOIN VALUE TO EURO, DOLAR AND REAL.
EACH CURRENCY IS SAVED TO A DIFFERENT FILE
"""
class Application:
    def __init__(self):

        #KEEPING THIS RUNNING WHILE APP IS RUNNING
        on = True
        while on:

            #THIS GET_VALUE FUNCTION IS SAVED ON THE FILE BTC.PY
            #YOU JUST NEED TO PASS THE CURRENCY AND ANY NUMERIC STRING.
            euro = get_value("EUR", "1")
            dolar = get_value("USD", "1")
            real = get_value("BRL", "1")

            #OPENING FILES AND SAVING INFO TO THEM
            f_euro = open("btc_to_euro.txt", 'a')
            f_euro.write(str(datetime.datetime.now()) + "----" + euro + "\n")
            f_euro.close()

            f_dolar = open("btc_to_dolar.txt", 'a')
            f_dolar.write(str(datetime.datetime.now()) + "----" + dolar + "\n")
            f_dolar.close()

            f_dolar = open("btc_to_real.txt", 'a')
            f_dolar.write(str(datetime.datetime.now()) + "----" + real + "\n")
            f_dolar.close()
            time.sleep(30)


#CALLING APPLICATION CLASS
app = Application()



