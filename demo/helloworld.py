#!/usr/bin/python3
from caya.core import *
from caya.font8x8 import *

class myApp(CAYA):
	def setup(self):
		self.setSize((128,128),(256,256))
		self.setTitle("hello world")
		self.setIcon("res/snake.png")
		
		font = Font(self)
		self.img = font.createStrImage("Hello world\n Enjoy CAYA!")

	def loop(self):
		self.clear()
		self.put(self.img, 64, 64, center=True)

if __name__ == "__main__":
	myApp()
