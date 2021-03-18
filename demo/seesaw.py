#!/usr/bin/python3
from caya.core import *
from caya.font8x8 import *
import math

class myApp(CAYA):
	def setup(self):
		self.setSize((128,128),(256,256))
		self.setTitle("hello world")
		self.setIcon("res/snake.png")
		
		font = Font(self)
		self.img = font.createStrImage("SeeSaw!")
		
		self.r = 0

	def loop(self):
		self.clear()
		rr = math.cos(math.radians(self.r)) * 45
		self.put(self.img, 64, 64, center=True, rotate=rr, scale=2)
		self.r = (self.r + 0.5) % 360

if __name__ == "__main__":
	myApp()
