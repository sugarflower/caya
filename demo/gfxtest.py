from caya import *
import random


class myApp(CAYA):

    def rint(self, maxvalue):
        return random.randint(0, maxvalue)

    def rpos(self):
        return self.rint(self.config["display"]["real"]["w"])

    def rcol(self):
        return self.rint(255)


    def setup(self):
        self.setTitle("gfx test")
        self.setIcon("res/snake.png")
        self.step = 0


    def loop(self):
        colour = (self.rcol(), self.rcol(), self.rcol(), self.rcol())
        line(self.getSurface(), self.rpos(), self.rpos(), self.rpos(), self.rpos(), colour)
        filled_circle(self.getSurface(), self.rpos(), self.rpos(), self.rpos(), colour)

        self.step += 1
        if self.step == 2048:
            self.clear()
            self.step = 0

if __name__ == "__main__":
    myApp()
