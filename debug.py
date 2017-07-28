import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from threading import Thread

import usbtinyisp

from pdb import set_trace

samples = 1000
channels = 4

fig, ax = plt.subplots()
ydata = np.zeros([samples, channels])
lns = plt.plot(ydata)

tiny = usbtinyisp.usbtiny()
tiny.power_on()

def aquire():
    global ydata
    while True:
        ydata = np.roll(ydata, -1, 0)
        for j in range(channels):
            dat = tiny.spi1(0)
            ydata[-1, j] = dat[0]

th = Thread(target=aquire)
th.daemon = True
th.start()

def init():
    ax.set_ylim(0, 255)
    ax.set_xlim(0, samples)
    return lns

def update(frame):
    #set_trace()
    for ln, dat in zip(lns, ydata.T):
        ln.set_ydata(dat)

    return lns

ani = FuncAnimation(fig, update, interval=100,
                    init_func=init, blit=True)
plt.show()
