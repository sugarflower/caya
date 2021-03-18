#!/usr/bin/python3
from caya.core import *

class myApp(CAYA):
	def setup(self):
		self.setSize((255,128))
		self.setTitle("Simple")
		self.setIcon("res/snake.png")

	def loop(self):
		pass

if __name__ == "__main__":
	myApp()
