# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:10:29 2020

@author: 18134
"""


import numpy as np
import matplotlib.pyplot as plot

x = np.arange(500) / 500 - 0.5
y = np.arange(500) / 500 - 0.5

X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
f0 = 100
k = 2500
a = np.cos(np.pi * 2 * (f0 * R + k * R**2 / 2))

fig, ax = plot.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='nearest', cmap='RdYlGn_r')
ax.set_title("Cosine Function interpolation to the nearest")
plot.show()

