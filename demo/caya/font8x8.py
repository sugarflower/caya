#!/usr/bin/python3
from caya.core import *

class Font:
    font8x8_basic = (
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x18, 0x3C, 0x3C, 0x18, 0x18, 0x00, 0x18, 0x00),   
        ( 0x36, 0x36, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x36, 0x36, 0x7F, 0x36, 0x7F, 0x36, 0x36, 0x00),   
        ( 0x0C, 0x3E, 0x03, 0x1E, 0x30, 0x1F, 0x0C, 0x00),   
        ( 0x00, 0x63, 0x33, 0x18, 0x0C, 0x66, 0x63, 0x00),   
        ( 0x1C, 0x36, 0x1C, 0x6E, 0x3B, 0x33, 0x6E, 0x00),   
        ( 0x06, 0x06, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x18, 0x0C, 0x06, 0x06, 0x06, 0x0C, 0x18, 0x00),   
        ( 0x06, 0x0C, 0x18, 0x18, 0x18, 0x0C, 0x06, 0x00),   
        ( 0x00, 0x66, 0x3C, 0xFF, 0x3C, 0x66, 0x00, 0x00),   
        ( 0x00, 0x0C, 0x0C, 0x3F, 0x0C, 0x0C, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x0C, 0x06),   
        ( 0x00, 0x00, 0x00, 0x3F, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x0C, 0x00),   
        ( 0x60, 0x30, 0x18, 0x0C, 0x06, 0x03, 0x01, 0x00),   
        ( 0x3E, 0x63, 0x73, 0x7B, 0x6F, 0x67, 0x3E, 0x00),   
        ( 0x0C, 0x0E, 0x0C, 0x0C, 0x0C, 0x0C, 0x3F, 0x00),   
        ( 0x1E, 0x33, 0x30, 0x1C, 0x06, 0x33, 0x3F, 0x00),   
        ( 0x1E, 0x33, 0x30, 0x1C, 0x30, 0x33, 0x1E, 0x00),   
        ( 0x38, 0x3C, 0x36, 0x33, 0x7F, 0x30, 0x78, 0x00),   
        ( 0x3F, 0x03, 0x1F, 0x30, 0x30, 0x33, 0x1E, 0x00),   
        ( 0x1C, 0x06, 0x03, 0x1F, 0x33, 0x33, 0x1E, 0x00),   
        ( 0x3F, 0x33, 0x30, 0x18, 0x0C, 0x0C, 0x0C, 0x00),   
        ( 0x1E, 0x33, 0x33, 0x1E, 0x33, 0x33, 0x1E, 0x00),   
        ( 0x1E, 0x33, 0x33, 0x3E, 0x30, 0x18, 0x0E, 0x00),   
        ( 0x00, 0x0C, 0x0C, 0x00, 0x00, 0x0C, 0x0C, 0x00),   
        ( 0x00, 0x0C, 0x0C, 0x00, 0x00, 0x0C, 0x0C, 0x06),   
        ( 0x18, 0x0C, 0x06, 0x03, 0x06, 0x0C, 0x18, 0x00),   
        ( 0x00, 0x00, 0x3F, 0x00, 0x00, 0x3F, 0x00, 0x00),   
        ( 0x06, 0x0C, 0x18, 0x30, 0x18, 0x0C, 0x06, 0x00),   
        ( 0x1E, 0x33, 0x30, 0x18, 0x0C, 0x00, 0x0C, 0x00),   
        ( 0x3E, 0x63, 0x7B, 0x7B, 0x7B, 0x03, 0x1E, 0x00),   
        ( 0x0C, 0x1E, 0x33, 0x33, 0x3F, 0x33, 0x33, 0x00),   
        ( 0x3F, 0x66, 0x66, 0x3E, 0x66, 0x66, 0x3F, 0x00),   
        ( 0x3C, 0x66, 0x03, 0x03, 0x03, 0x66, 0x3C, 0x00),   
        ( 0x1F, 0x36, 0x66, 0x66, 0x66, 0x36, 0x1F, 0x00),   
        ( 0x7F, 0x46, 0x16, 0x1E, 0x16, 0x46, 0x7F, 0x00),   
        ( 0x7F, 0x46, 0x16, 0x1E, 0x16, 0x06, 0x0F, 0x00),   
        ( 0x3C, 0x66, 0x03, 0x03, 0x73, 0x66, 0x7C, 0x00),   
        ( 0x33, 0x33, 0x33, 0x3F, 0x33, 0x33, 0x33, 0x00),   
        ( 0x1E, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x1E, 0x00),   
        ( 0x78, 0x30, 0x30, 0x30, 0x33, 0x33, 0x1E, 0x00),   
        ( 0x67, 0x66, 0x36, 0x1E, 0x36, 0x66, 0x67, 0x00),   
        ( 0x0F, 0x06, 0x06, 0x06, 0x46, 0x66, 0x7F, 0x00),   
        ( 0x63, 0x77, 0x7F, 0x7F, 0x6B, 0x63, 0x63, 0x00),   
        ( 0x63, 0x67, 0x6F, 0x7B, 0x73, 0x63, 0x63, 0x00),   
        ( 0x1C, 0x36, 0x63, 0x63, 0x63, 0x36, 0x1C, 0x00),   
        ( 0x3F, 0x66, 0x66, 0x3E, 0x06, 0x06, 0x0F, 0x00),   
        ( 0x1E, 0x33, 0x33, 0x33, 0x3B, 0x1E, 0x38, 0x00),   
        ( 0x3F, 0x66, 0x66, 0x3E, 0x36, 0x66, 0x67, 0x00),   
        ( 0x1E, 0x33, 0x07, 0x0E, 0x38, 0x33, 0x1E, 0x00),   
        ( 0x3F, 0x2D, 0x0C, 0x0C, 0x0C, 0x0C, 0x1E, 0x00),   
        ( 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x3F, 0x00),   
        ( 0x33, 0x33, 0x33, 0x33, 0x33, 0x1E, 0x0C, 0x00),   
        ( 0x63, 0x63, 0x63, 0x6B, 0x7F, 0x77, 0x63, 0x00),   
        ( 0x63, 0x63, 0x36, 0x1C, 0x1C, 0x36, 0x63, 0x00),   
        ( 0x33, 0x33, 0x33, 0x1E, 0x0C, 0x0C, 0x1E, 0x00),   
        ( 0x7F, 0x63, 0x31, 0x18, 0x4C, 0x66, 0x7F, 0x00),   
        ( 0x1E, 0x06, 0x06, 0x06, 0x06, 0x06, 0x1E, 0x00),   
        ( 0x03, 0x06, 0x0C, 0x18, 0x30, 0x60, 0x40, 0x00),   
        ( 0x1E, 0x18, 0x18, 0x18, 0x18, 0x18, 0x1E, 0x00),   
        ( 0x08, 0x1C, 0x36, 0x63, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF),   
        ( 0x0C, 0x0C, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x1E, 0x30, 0x3E, 0x33, 0x6E, 0x00),   
        ( 0x07, 0x06, 0x06, 0x3E, 0x66, 0x66, 0x3B, 0x00),   
        ( 0x00, 0x00, 0x1E, 0x33, 0x03, 0x33, 0x1E, 0x00),   
        ( 0x38, 0x30, 0x30, 0x3e, 0x33, 0x33, 0x6E, 0x00),   
        ( 0x00, 0x00, 0x1E, 0x33, 0x3f, 0x03, 0x1E, 0x00),   
        ( 0x1C, 0x36, 0x06, 0x0f, 0x06, 0x06, 0x0F, 0x00),   
        ( 0x00, 0x00, 0x6E, 0x33, 0x33, 0x3E, 0x30, 0x1F),   
        ( 0x07, 0x06, 0x36, 0x6E, 0x66, 0x66, 0x67, 0x00),   
        ( 0x0C, 0x00, 0x0E, 0x0C, 0x0C, 0x0C, 0x1E, 0x00),   
        ( 0x30, 0x00, 0x30, 0x30, 0x30, 0x33, 0x33, 0x1E),   
        ( 0x07, 0x06, 0x66, 0x36, 0x1E, 0x36, 0x67, 0x00),   
        ( 0x0E, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x1E, 0x00),   
        ( 0x00, 0x00, 0x33, 0x7F, 0x7F, 0x6B, 0x63, 0x00),   
        ( 0x00, 0x00, 0x1F, 0x33, 0x33, 0x33, 0x33, 0x00),   
        ( 0x00, 0x00, 0x1E, 0x33, 0x33, 0x33, 0x1E, 0x00),   
        ( 0x00, 0x00, 0x3B, 0x66, 0x66, 0x3E, 0x06, 0x0F),   
        ( 0x00, 0x00, 0x6E, 0x33, 0x33, 0x3E, 0x30, 0x78),   
        ( 0x00, 0x00, 0x3B, 0x6E, 0x66, 0x06, 0x0F, 0x00),   
        ( 0x00, 0x00, 0x3E, 0x03, 0x1E, 0x30, 0x1F, 0x00),   
        ( 0x08, 0x0C, 0x3E, 0x0C, 0x0C, 0x2C, 0x18, 0x00),   
        ( 0x00, 0x00, 0x33, 0x33, 0x33, 0x33, 0x6E, 0x00),   
        ( 0x00, 0x00, 0x33, 0x33, 0x33, 0x1E, 0x0C, 0x00),   
        ( 0x00, 0x00, 0x63, 0x6B, 0x7F, 0x7F, 0x36, 0x00),   
        ( 0x00, 0x00, 0x63, 0x36, 0x1C, 0x36, 0x63, 0x00),   
        ( 0x00, 0x00, 0x33, 0x33, 0x33, 0x3E, 0x30, 0x1F),   
        ( 0x00, 0x00, 0x3F, 0x19, 0x0C, 0x26, 0x3F, 0x00),   
        ( 0x38, 0x0C, 0x0C, 0x07, 0x0C, 0x0C, 0x38, 0x00),   
        ( 0x18, 0x18, 0x18, 0x00, 0x18, 0x18, 0x18, 0x00),   
        ( 0x07, 0x0C, 0x0C, 0x38, 0x0C, 0x0C, 0x07, 0x00),   
        ( 0x6E, 0x3B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
        ( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))

    def __init__(self,pyg):
        self.pyg = pyg
        self.size = { "x":8, "y":8 }
        self.position=(0,0)
        self.color = (255,255,255,255)

    def _getFontData(self, asc, color):
        buf = bytearray(256)
        dat = self.font8x8_basic[asc]
        for j in range(8):
            for i in range(8):
                idx = ((j<<3)+i)<<2
                if (dat[j] >> i) & 1 != 0:
                    buf[idx]   = color[0] #A 
                    buf[idx+1] = color[1] #R
                    buf[idx+2] = color[2] #G
                    buf[idx+3] = color[3] #B
              
        return buf

    def setPos(self, x, y):
        self.position = (x, y)

    def getPos(self):
        return self.position

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def putChr(self, asc, pos=None, surf=None):
        buf = self._getFontData(asc,self.getColor())
        if pos == None:
            pos = self.getPos()
        if surf == None:
            surf = self.pyg.getSurface()
        img = image.frombuffer(buf, (self.size["x"],self.size["y"]), "ARGB")
        self.pyg.put(img, pos[0], pos[1], surface=surf)

    def printStr(self,strvar,surf=None, pos=None, color=None):
        if pos != None:
            self.setPos(pos[0],pos[1])
        if color != None:
            self.setColor(color)
        b = strvar.encode()
        for s in b:
            self.putChr(s,surf=surf)
            pos=self.getPos()
            self.setPos(pos[0]+self.size["x"],pos[1])

    def createStrImage(self, strvar, pos=None, color=None):
        strbuf = strvar.split("\n")
        w = 0
        h = 0
        for s in strbuf:
            h += 1
            if w < len(s):
                w = len(s)

        w *= 8
        h *= 8
        surf = Surface((w, h), SWSURFACE | SRCALPHA, 32)

        y = 0
        for s in strbuf:
            self.printStr(s, surf=surf, pos=(0, y*8), color=color)
            y += 1
        return surf

            

