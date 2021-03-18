from caya import *
import random

class myApp(CAYA):

    def setup(self):
        self.setSize((512,256))
        self.setTitle("Multi Touch Test")
        self.setIcon("res/snake.png")
        circles = {}

    def loop(self):
        self.fill((0,0,0,1))
        
        tn = self.getTouchs()
        if tn > 0:
            for n in range(tn):
                x, y = self.getTouchPos(n)

                filled_circle(self.getSurface(), x, y, 10,(200,0,200))
        
        
        pass

if __name__ == "__main__":
    myApp()
