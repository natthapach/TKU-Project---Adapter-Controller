import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("log.csv","r").read()
    dataArray = pullData.split('\n')
    dataArray = dataArray[-50:]
    px = 0
    py = 0
    pz = 0
    order = []
    xvalue = []
    yvalue = []
    zvalue = []
    i = 0
    for eachLine in dataArray:
        if len(eachLine)>1:
            line = eachLine.split(',')
            x = float(line[0])
            y = float(line[1])
            z = float(line[2])
            dx = x - px
            dy = y - py
            dz = z - pz
            px = x
            py = y
            pz = z
            order.append(i)
            xvalue.append(dx)
            yvalue.append(dy)
            zvalue.append(dz)
            i += 1
    ax1.clear()
    ax1.plot(order,xvalue)
    ax1.plot(order,yvalue)
    ax1.plot(order,zvalue)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()