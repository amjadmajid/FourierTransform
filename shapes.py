import numpy as np
class Circle:
	def __init__(self, radius=1, dots=100):
		self.radius=radius
		self.dots=dots

	def xy_coordinate(self):
		pts = self.radius * np.exp(2j*np.pi * np.linspace(0,1,self.dots) )
		return pts.real , pts.imag

class Sine:
	def __init__(self, amplitude=1, freq=1, time=1, dots=100):
		self.amp = amplitude
		self.freq = freq
		self.time = time
		self.dots = dots


	def xy_coordinate(self):
		x = np.linspace(0,self.time,self.dots*self.time)
		return x, self.amp * np.sin( 2 * np.pi * self.freq * x )
