# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:34:00 2020

@author: 18134
"""

import mpl_toolkits.mplot3d 
from mpl_toolkits.mplot3d import axes3d
import matplotlib
from matplotlib import pyplot as plot
import numpy as np

fig = plot.figure()
ax = fig.add_subplot(111, projection = "3d")

x =np.arange(0,100)
y =np.cos(x)
z =np.cos(y)

ax.scatter(x, y, z, c='r', marker='p')


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plot.show()

