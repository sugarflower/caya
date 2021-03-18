#!/usr/bin/python3
from caya.core import *
from caya.font8x8 import *
import math
from operator import itemgetter


class myApp(CAYA):

	def rot(self, w, h, r):
		dw = w * math.cos(math.radians(r)) - h * math.sin(math.radians(r))
		dh = w * math.sin(math.radians(r)) + h * math.cos(math.radians(r))
		return dw,dh


	def setup(self):
		self.setSize((256,128),(512,256))
		self.setTitle("3D Demo")
		self.setIcon("res/snake.png")
		
		self.ball = self.loadImage("res/ball.png")
		self.font = Font(self)

		msg = "Welcome to pyg!\npyg is an easy-to-use solution\nfor PyGame."
		self.msgImg = self.font.createStrImage(msg, Color(255,255,255))

		self.ra = 0
		self.rb = 0
		self.rc = 0
		self.rd = 0
		
		self.b = [[(x - 2) * 2, (y - 2) * 2, (z - 2) * 2]
                          for x in range(5) for y in range(5) for z in range(5)]


	def loop(self):
		self.clear()

		rc = math.cos(math.radians(self.rc)) * 2 + 3
		rd = math.cos(math.radians(self.rd)) * 5

		bb = [ [0, 0, 0] ] * 5 * 5 * 5
		for z in range(5):
			for y in range(5):
				for x in range(5):
					idx = z * 25 + y * 5 + x
					xx, yy = self.rot(self.b[idx][0] * rc, self.b[idx][1] * rc, self.ra)
					xx, zz = self.rot(xx,                  self.b[idx][2] * rc, self.rb)
					zz = zz + 20 
					xx = int(xx * zz * 0.33 ) + 128
					yy = int(yy * zz * 0.33 ) + 64

					bb[idx] = [xx, yy, zz]

		bb = sorted( bb, key=itemgetter(2) )			

		for i in range(125):
			self.put(self.ball, bb[i][0], bb[i][1], scale=bb[i][2] * 0.066, center=True)

		del bb

		self.ra = (self.ra + 0.4) % 360
		self.rb = (self.rb + 0.1) % 360
		self.rc = (self.rc + 0.1) % 360
		self.rd = (self.rd + 0.2) % 360

		self.put(self.msgImg, 128, 64, center=True,rotate=rd)
		self.put(self.font.createStrImage("%04.4f" % self.ra, color=(255,150,250,50)),0 ,0 )
		self.put(self.font.createStrImage("%04.4f" % self.rb, color=(255,150,250,50)),0 ,8 )
		self.put(self.font.createStrImage("%04.4f" % rc,      color=(255,250,250,50)),0 ,16)


if __name__ == "__main__":
	myApp()

