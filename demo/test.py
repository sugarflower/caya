#!/usr/bin/python3
from caya.core import *
from caya.font8x8 import *
import random

class myApp(CAYA):

	def setup(self):
		self.setSize((160,160),(320,320))
		self.setTitle("PYG2 Test")
		self.setIcon("res/snake.png")
		
		self.img = self.loadImage("res/pic.png")
		
		font = Font(self)
		self.img_shake = font.createStrImage("Shake")
		self.img_flip  = font.createStrImage("Flip")
		self.img_rot   = font.createStrImage("Rotate")
                
		msg = "Let'sTry MouseMotion\n\"ESC\" Quit App."
		self.img_msg = font.createStrImage(msg)

		self.sp = {
			"player":(0,0,8,8),
			"tomato":(8,0,8,8),
			"block":(16,0,8,8),
			}

	def loop(self):
		self.clear()
		self.fill(Color(100,0,0))
		

		self.put(self.img,0,0)

		self.put(self.img_flip,0,16)
		self.put(self.img, 0,24,  self.sp["tomato"])
		self.put(self.img, 8,24,  self.sp["tomato"], flip=FLIP_H)
		self.put(self.img, 16,24, self.sp["tomato"], flip=FLIP_V)
		self.put(self.img, 24,24, self.sp["tomato"], flip=FLIP_BOTH)

		self.put(self.img_rot, 0,40)
		self.put(self.img, 0,48, self.sp["player"], rotate=90)
		self.put(self.img, 8,48, self.sp["player"], rotate=180)
		self.put(self.img, 16,48,self.sp["player"], rotate=270)

		pos = self.getMousePos()
		self.put(self.img, pos[0], pos[1], self.sp["player"])
		
		if self.isPress():
			self.setOffset(random.randint(0,10)-5,random.randint(0,10)-5)
			self.put(self.img_shake,80,80,center=True)
		else:
			self.setOffset(0,0)
			

		self.put(self.img_msg, 0,136)

		"""
		e = p.getEvent()
		if e != None:
			print(e)
			if e.type == 6:
				print(e.button)
		"""
		if self.isAnyKeyDown():
			print(self.data["keys"])

myApp()

