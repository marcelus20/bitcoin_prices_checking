import matplotlib.pyplot as plt
import datetime
import re

class Plotting:
    def __init__(self):
        self.show_plot()


    def read_files(self, file):
        f = open(file)
        lines = []

        for eachLine in f.read().split("\n"):
            if len(eachLine) > 0:
                lines.append(eachLine)

        f.close()
        return lines

    def show_plot(self):

        dolar = self.read_files("btc_to_dolar.txt")
        euro = self.read_files("btc_to_euro.txt")
        real = self.read_files("btc_to_real.txt")

        time = []
        for dates in dolar:
            time.append(datetime.datetime.strptime(dates.split("----")[0],
                                                   "%Y-%m-%d %H:%M:%S.%f"))

    def date_formater(self, str):
        if re.match(r'\d\d/\d\d/\d\d\d\d', str):
            return str
        if re.match(r'\d\d\d\d\d\d\d\d', str):
            text = ""
            for i in range(len(str)):
                if i == 2 or i == 4:
                    text +="/"
                text+=str[i]
            return text



plot = Plotting()

plot.date_formater("11112012")