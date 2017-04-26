import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from jnpr.junos import Device
import time
import numpy as np
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(10))
ax.set_ylim(0, 25)
data = [0]*10


dev = Device(host='172.27.0.159', user='rbindra', password='N0c@nd00', gather_facts=False)
dev.open()


def update(i):
    time.sleep(0.5)
    op = dev.rpc.get_route_engine_information({'format': 'json'})
    cpu_data = op['route-engine-information'][0]['route-engine'][0]
    data.pop(0)
    data.append(int(cpu_data['cpu-system'][0].get('data')))
    line.set_ydata(data)
    return line,

ani = animation.FuncAnimation(fig, update, interval=100)
#plt.show()
plt.savefig("/var/tmp/node.png")
