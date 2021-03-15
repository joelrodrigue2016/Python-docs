# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:03:10 2020

@author: 18134
"""

#this is a simple pong game
#https://www.youtube.com/watch?v=XGf2GcyHPhc

import turtle
import os
wn = turtle.Screen()
wn.title("Pong by Joel Rodriguez")
wn.bgcolor("black")
wn.setup(width= 800, height = 600)
wn.tracer(0)


    
# Paddle 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")   
paddle_a.penup()
paddle_a.goto(-350, 0)

    
# Paddle B
    
    
# Ball


# main loop
while True:
    wn.update()
    