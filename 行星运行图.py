"""1700011739.py: Description of what foobar does.

__author__ = "Yida Jiang"
__pkuid__  = "1700011739"
__email__  = "1700011739@pku.edu.cn"
"""

import turtle
import math

def location(a,b,c,n):
    global t
    n.goto(a * math.cos(math.radians((360 * t / c))),b * math.sin(math.radians((360 * t / c))))

    
wn = turtle.Screen()
wn.bgcolor('black')

#set sun and planets
sun= turtle.Turtle()
sun.shapesize(2,2,1)
sun.color('red')
sun.shape('circle')

earth = turtle.Turtle()
earth.shapesize(1,1,0)
earth.color('blue')
earth.shape('circle')
earth.up()
earth.goto(152.1/2,0)
earth.down()

mercury = turtle.Turtle()
mercury.shapesize(0.38,0.38,0)
mercury.color('light blue')
mercury.shape('circle')
mercury.up()
mercury.goto(69.8/2,0)
mercury.down()

venus= turtle.Turtle()
venus.shapesize(0.95,0.95,0)
venus.color('yellow')
venus.shape('circle')
venus.up()
venus.goto(108.9/2,0)
venus.down()

mars= turtle.Turtle()
mars.shapesize(0.53,0.53,0)
mars.color('red')
mars.shape('circle')
mars.up()
mars.goto(249.2/2,0)
mars.down()

jupyter= turtle.Turtle()
jupyter.shapesize(2.8,2.8,0)
jupyter.color('orange')
jupyter.shape('circle')
jupyter.up()
jupyter.goto(816.6/4,0)
jupyter.down()

saturn= turtle.Turtle()
saturn.shapesize(9.41/4,9.41/4,0)
saturn.color('gray')
saturn.shape('circle')
saturn.up()
saturn.goto(1514.5/5,0)
saturn.down()

earth.left(90)


t=1
while t>0:
    location(152.1/2,147.1/2,100,earth)
    location(69.8/2,46.0/2,24,mercury)
    location(108.9/2,107.5/2,61.5,venus)
    location(249.2/2,206.7/2,188,mars)
    location(816.6/4,740.5/4,1186,jupyter)
    location(1514.5/5,1352.5/5,2946,saturn)
    t += 1
