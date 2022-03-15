import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from shapes import * 

fig, ax = plt.subplots()

x,y = Circle(dots=200).xy_coordinate()
x_sin,y_sin = Sine(freq=4, time=2).xy_coordinate()

ax.plot(x,y, '*')
ax.plot(x_sin,y_sin, color="green",) 
dot, = ax.plot(0, '*', color='red')

# animate 
def animate_frame(i):
	pts = np.exp(2j*np.pi/100 * -i)
	dot.set_data(pts.real, pts.imag)
	return dot,
		

animation = FuncAnimation(fig, func=animate_frame, frames=np.arange(0,101), interval=80)
ax.set_aspect(1)
plt.show()
