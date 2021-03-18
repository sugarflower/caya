from pygame import *
from pygame.locals import *

#from pygame.camera import *
#https://www.lfd.uci.edu/~gohlke/pythonlibs/#videocapture

#import pygame.gfxdraw as gfx
from pygame.gfxdraw import *
import time, os
from caya.dataobj import *

FLIP_H = 1
FLIP_V = 2
FLIP_BOTH = 3

class CAYAData(DataObj):
    def __init__(self):
        super().__init__()
        self.new()
        
    def read(self):
        pass

    def save(self):
        pass


class CAYA:
    
    def __init__(self):
        self.data = CAYAData()
        self.config = CAYAData()
        mixer.pre_init( 44100, -16, 2, 1024)
        mixer.init()
        init()
        joystick.init()
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        os.environ['SDL_MOUSE_TOUCH_EVENTS'] = '1'

        self.config["mode"] = SWSURFACE
        self.config["waittime"] = 0.016
        self.config["display"] = {
            "real":   { "w": 128, "h": 128},
            "disp":   { "w": 384, "h": 384},
            "margin": { "h": 20,  "v": 20 }
            }
        self.data["mouse"] = {
            "position": { "x": 0, "y": 0 },
            "button": [False] * 3,
            "click": [False] * 3,
            "disp": False
            }
        self.data["finger"] = []
        self.data["offset"] = {"x": 0, "y": 0}
        self.data["running"] = True
        self.data["keys"] = []
        self.data["procwait"] = True
        self.data["fullscreen"] = False

        self.setupDisplay()
        self.setup()
        self.mainloop()

    def setup(self):
        pass

    def loop(self):
        pass

    def quit(self):
        self.data["running"] = False

    def mainloop(self):
        while self.data["running"]:
            self.data["mouse"]["click"] = [False] * 3
            self.data["procwait"] = True
            st = time.time()
            while self.data["procwait"]:
                time.sleep(0.001)
                for e in event.get():
                    self.events(e)
                self.loop()

                if time.time() - st > self.config["waittime"]:
                    self.data["procwait"] = False
                    self.update()
        
        mixer.stop()
        mixer.quit()
        joystick.quit()
        quit()

    #-------------------------------------------------------------------

    def events(self, e):
        if e.type == QUIT:
            self.data["running"] = False

        if e.type == KEYDOWN:
            k = e.key
            if not k in self.data["keys"]:
                self.data["keys"].append(k)

        if e.type == KEYUP:
            
            if self.isKeyDownCode( 91 ):
                if self.config["fullscreen"]:
                    self.setFullscreen(False)
                else:
                    self.setFullscreen(True)

            if self.isKeyDownCode(27):
                self.data["running"] = False
                    
            for idx,k in enumerate(self.data["keys"]):
                if k == e.key:
                    self.data["keys"].pop(idx)
                    break;

        if e.type == MOUSEMOTION:
            self.data["mouse"]["position"]["x"] = e.pos[0]
            self.data["mouse"]["position"]["y"] = e.pos[1]

        if e.type == MOUSEBUTTONDOWN:
            self.data["mouse"]["button"] = mouse.get_pressed()

        if e.type == MOUSEBUTTONUP:
            self.data["mouse"]["click"] = self.data["mouse"]["button"]
            self.data["mouse"]["button"] = [False] * 3

        if e.type == FINGERMOTION:
            for idx, f in enumerate(self.data["finger"]):
                if f["id"] == e.finger_id:
                    self.data["finger"][idx] = {
                            "id": f["id"],
                            "x": e.x,
                            "y": e.y,
                            "dx": e.dx,
                            "dy": e.dy,
                            "pressure": e.pressure
                        }

        if e.type == FINGERDOWN:
            self.data["finger"].append({
                    "id": e.finger_id,
                    "x": e.x,
                    "y": e.y,
                    "dx": e.dx,
                    "dy": e.dy,
                    "pressure": e.pressure
                })
            #print(self.data["finger"])

        if e.type == FINGERUP:
            for idx, f in enumerate(self.data["finger"]):
                if f["id"] == e.finger_id:
                    self.data["finger"].pop(idx)

    #-------------------------------------------------------------------

    def setupDisplay(self):
        self.config["display"]["size"] = {
                "w": self.config["display"]["disp"]["w"] + (self.config["display"]["margin"]["h"] * 2),
                "h": self.config["display"]["disp"]["h"] + (self.config["display"]["margin"]["h"] * 2)}
        if self.config["fullscreen"]:
            self.data["screen"] = display.set_mode(
                (self.config["display"]["size"]["w"], self.config["display"]["size"]["h"]),
                self.config["mode"] | FULLSCREEN)
        else:
            self.data["screen"] = display.set_mode(
                (self.config["display"]["size"]["w"], self.config["display"]["size"]["h"]),
                self.config["mode"])     
        self.data["surface"] = Surface(
            (self.config["display"]["real"]["w"], self.config["display"]["real"]["h"]),
            self.config["mode"] | SRCALPHA, 32)

        self.dispMouseCursor(self.data["mouse"]["disp"])

    def dispMouseCursor(self, flg):
            self.data["mouse"]["disp"] = flg
            mouse.set_visible(flg)

    def update(self):
        buf = self.createSurface(self.config["display"]["real"]["w"], self.config["display"]["real"]["h"])
        buf.blit(self.getSurface(),(self.data["offset"]["x"], self.data["offset"]["y"]) )
        self.getScreen().blit(transform.scale(buf,
            (self.config["display"]["disp"]["w"], self.config["display"]["disp"]["h"])),
            (self.config["display"]["margin"]["h"], self.config["display"]["margin"]["v"]))
        display.update()

    def setSize(self, real, disp=None, margin=None):
        self.config["display"]["real"]["w"] = real[0]
        self.config["display"]["real"]["h"] = real[1]
        if not disp == None:
            self.config["display"]["disp"]["w"] = disp[0]
            self.config["display"]["disp"]["h"] = disp[1]
        else:
            self.config["display"]["disp"]["w"] = self.config["display"]["real"]["w"]
            self.config["display"]["disp"]["h"] = self.config["display"]["real"]["h"]
        if not margin == None:
            self.config["display"]["margin"]["h"] = margin[0]
            self.config["display"]["margin"]["v"] = margin[1]
        self.setupDisplay()

    def setOffset(self, x, y):
        self.data["offset"]["x"] = x
        self.data["offset"]["y"] = y

    def setFullscreen(self, flg):
        self.config["fullscreen"] = flg
        self.setupDisplay()

    def setTitle(self, title):
        display.set_caption(title)

    def setWaitTime(self, waittime=0.016):
        self.config["waittime"] = waittime

    def setIcon(self, imagepath):
        img = self.loadImage(imagepath)
        display.set_icon(img)
        
    #-------------------------------------------------------------------

    def clear(self):
        self.fill((0,0,0,0), self.getSurface() )
        self.fill((0,0,0), self.getScreen() )

    def fill(self, color=(0,0,0,0), surface=None):
        if surface == None:
            surface = self.getSurface()
        surface.fill(color)

    def createSurface(self, w, h):
        return Surface((w, h), self.config["mode"] | SRCALPHA, 32)

    def loadImage(self, imagepath):
        return image.load(imagepath).convert_alpha()

    def createImage(self, w, h):
        return Surface((w, h), self.config["mode"] | SRCALPHA, 32)

    def getSurface(self):
        return self.data["surface"]

    def getScreen(self):
        return self.data["screen"]

    def put(self, img, pos_x, pos_y, rect=None, flip=None, rotate=None, surface=None, scale=None, center=False):
        if surface == None:
            surface = self.getSurface()

        if rect == None:
            imgrect = ( 0, 0, img.get_width(), img.get_height() )
        else:
            imgrect = rect

        surftemp = Surface( (imgrect[2],imgrect[3]), self.config["mode"] | SRCALPHA, 32 )
        surftemp.blit(img, dest=(0,0), area=imgrect)
        
        if not flip == None:
            if flip == FLIP_H:
                surftemp = transform.flip(surftemp, True, False)
            elif flip == FLIP_V:
                surftemp = transform.flip(surftemp, False, True)
            elif flip == FLIP_BOTH:
                surftemp = transform.flip(surftemp, True, True)

        if not scale == None:
            if type(scale) in( int, float ):
                scale = (scale,scale)
            sc = (int(surftemp.get_width()*abs(scale[0])), int(surftemp.get_height()*abs(scale[1])))
            if scale[0] > 1 or scale[1] > 1:
                surftemp2 = transform.scale(surftemp, sc)
            else:
                surftemp2 = transform.smoothscale(surftemp, sc)
        else:
            surftemp2 = surftemp

        w = surftemp2.get_width()
        h = surftemp2.get_height()
        if not rotate == None:
            rotate = (360 - rotate) % 360
            surftemp3 = transform.rotate(surftemp2, rotate)
            dw = int((w - surftemp3.get_width())) // 2
            dh = int((h - surftemp3.get_height())) // 2
        else:
            surftemp3 = surftemp2
            dw = 0
            dh = 0
        
        if center:
            surface.blit(surftemp3, (pos_x + dw - (w//2), pos_y + dh - (h//2)))
        else:
            surface.blit(surftemp3, (pos_x + dw, pos_y + dh))

        del surftemp3
        del surftemp2
        del surftemp

    #-------------------------------------------------------------------

    def isKeyDown(self, key):
        return ord(key) in self.data["keys"]

    def isKeyDownCode(self, key):
        return key in self.data["keys"]

    def isAnyKeyDown(self):
        return len(self.data["keys"]) > 0

    def isClick(self, button=0):
        return self.data["mouse"]["click"][button]

    def isPress(self, button=0):
        return self.data["mouse"]["button"][button]

    def getMousePos(self):
        wa = self.config["display"]["real"]["w"] / self.config["display"]["disp"]["w"]
        ha = self.config["display"]["real"]["h"] / self.config["display"]["disp"]["h"]
        mx = self.data["mouse"]["position"]["x"] - self.config["display"]["margin"]["h"]
        my = self.data["mouse"]["position"]["y"] - self.config["display"]["margin"]["v"]
        return( int(mx * wa), int(my * ha) )

    def getJoysticks(self):
        return [joystick.Joystick(x) for x in range(joystick.get_count())]


    def getTouchs(self):
        return len(self.data["finger"])

    def getTouch(self, idx):
        return self.data["finger"][idx]

    def getTouchPos(self, idx):
        t = self.getTouch(idx)
        wa = self.config["display"]["real"]["w"]
        ha = self.config["display"]["real"]["h"]
        mx = t["x"] * (wa + self.config["display"]["margin"]["h"]) - self.config["display"]["margin"]["h"]
        my = t["y"] * (ha + self.config["display"]["margin"]["v"]) - self.config["display"]["margin"]["v"]
        return( int(mx), int(my) )
