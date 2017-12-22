import matplotlib.pyplot as plt
from matplotlib import animation
import datetime


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#THIS ANIMATE FUNCTION WILL MAKE THE GRAPH UPDATE REALTIME EVERY 25 SECONDS
def animate(i):
    #READING FILES
    file_euro = open("btc_to_euro.txt", "r").read()
    file_dolar = open("btc_to_dolar.txt", "r").read()
    file_real = open("btc_to_real.txt", "r").read()

    #CREATING EMPTY ARRAYS
    time = []
    price_euro = []
    price_dolar = []
    price_real = []

    #FILLING THE ARRAYS
    for line in file_euro.split("\n"):
        if len(line)>1:
            time.append(datetime.datetime.strptime(line.split("----")[0], "%Y-%m-%d %H:%M:%S.%f"))
            price_euro.append(float(line.split("----")[1]))
    for line in file_dolar.split("\n"):
        if len(line) > 1:
            price_dolar.append(float(line.split("----")[1]))
    for line in file_real.split("\n"):
        if len(line) > 1:
            price_real.append(float(line.split("----")[1]))


    #PLOTTING THE RESULTS
    ax1.clear()
    ax1.plot(time, price_euro, label="Euro")
    ax1.plot(time, price_dolar, label="Dolar")
    ax1.plot(time, price_real, label="Real")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)
    ax1.get_yaxis().get_major_formatter().set_useOffset(False)

#CARRY OUT THE ANIMATION
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
#print(type(datetime.datetime.strptime("2017-12-21 22:04:21.404122", "%Y-%m-%d %H:%M:%S.%f")))




