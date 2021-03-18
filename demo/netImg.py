#!/usr/bin/python3
from caya.core import *
import urllib.request as net
import io
import random

class myApp(CAYA):
	def setup(self):
		self.setSize((512,250))
		self.setTitle("Net Image")
		self.setIcon("res/snake.png")
		
		imgAddr = "https://www.python.org/static/img/python-logo.png"
		res = net.urlopen( imgAddr ).read()
		imgfile = io.BytesIO( res )
		self.img = self.loadImage( imgfile )
		self.r = 0
                
	def loop(self):
		self.fill( Color(50,50,80) )
		self.put( self.img, 256, 128, center=True, rotate=self.r)
		self.r = (self.r + .1) % 360
		self.setOffset(random.randint(-10,10), random.randint(-10,10))

app = myApp()


