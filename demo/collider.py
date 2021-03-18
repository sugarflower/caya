from pyg import *
import random as rnd
pd = PYGData()

pd["a"] = {"x": 0, "y": 0, "w": 3, "h": 3}
pd["b"] = {}
for i in range(100):
    pd["b"][i] = {"x": rnd.randint(-10,10),
                  "y": rnd.randint(-10,10),
                  "w": 3, "h": 3}


def collidrect(a, b):
    if a["y"] >= b["y"]+b["h"]:
        return False
    elif a["x"]+a["w"] <= b["x"]:
        return False
    elif a["y"]+a["h"] <= b["y"]:
        return False
    elif a["x"] >= b["x"]+b["w"]:
        return False
    return True

hit = 0
for i in range(100):
    if collidrect(pd["a"], pd["b"][i]):
        hit += 1

print(hit)
    
