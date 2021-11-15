from caya import *
import random as rnd

class myApp(CAYA):

    def collidrect(self, a, b):
        if a["y"] >= b["y"]+b["h"]:
            return False
        elif a["x"]+a["w"] <= b["x"]:
            return False
        elif a["y"]+a["h"] <= b["y"]:
            return False
        elif a["x"] >= b["x"]+b["w"]:
            return False
        return True

    def setup(self):
        self.points = {}
        self.points["a"] = {"x": 58, "y": 58, "w": 10, "h": 10}
        self.spray()
        self.config["waittime"] = 0.2

    def spray(self):
        self.points["b"] = {}
        for i in range(100):
            self.points["b"][i] = {"x": rnd.randint(0, 127),
                                   "y": rnd.randint(0, 127),
                                   "w": rnd.randint(3, 5),
                                   "h": rnd.randint(3, 5)}

    def loop(self):
        self.clear()
        hit = 0
        for i in range(100):
            if self.collidrect(self.points["a"],
                               self.points["b"][i]):
                hit += 1
                color = (255, 0, 0)
            else:
                color = (100, 100, 100)
                
            box(self.getSurface(),
                (self.points["b"][i]["x"],
                 self.points["b"][i]["y"],
                 self.points["b"][i]["w"],
                 self.points["b"][i]["h"]),
                 color)

        self.spray()

        rectangle(self.getSurface(),
                  (self.points["a"]["x"],
                   self.points["a"]["y"],
                   self.points["a"]["w"],
                   self.points["a"]["h"]),
                  (255, 255, 255))
            
if __name__ == "__main__":
    myApp()
