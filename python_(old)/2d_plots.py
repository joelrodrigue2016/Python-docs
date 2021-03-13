# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 21:26:33 2020

@author: 18134
"""


import numpy as np
import matplotlib
from matplotlib import pyplot as plot
import pandas as pd
import random
import math as math
import scipy as sc





x = np.arange(-100,101,0.2)
y = (x**5)/5
plot.plot(x,y,"-b")
plot.title("asd")
plot.grid()
plot.legend("asd")
plot.plot([1,2,3])
plot.xlabel("asd00")
plot.ylabel("asd")
plot.show()




x = np.arange(-100,101,0.2)
y = x**2
plot.plot(x,y,"-g")
plot.title("x^2 function")
plot.legend("x2")
plot.grid()
plot.xlabel("x axis")
plot.ylabel("y axis")

plot.show()


x = np.arange(0,101,0.1)
y = np.cos(x)
plot.plot(x,y,"--r")
plot.grid()
plot.title("asd")
plot.legend("asd")
plot.plot(1,2,3, "--b")
plot.xlabel("asd00")
plot.ylabel("asd")
plot.show()