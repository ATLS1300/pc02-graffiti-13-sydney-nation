  
#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Sydney Nation
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

t = Turtle()
# glasses lenses
t.pensize(2)
t.penup()
t.goto(-17,96)
t.pendown()
t.circle(18)
t.penup()
t.goto(45,110)
t.pendown()
t.circle(17)
t.penup()
# glasses bridge
t.goto(0,120)
t.left(11)
t.pendown()
t.forward(27)
t.penup()
# glasses ear piece
t.goto(-34,113)
t.right(195)
t.pendown()
t.forward(54)
t.penup()

# scar
t.pensize(4)
t.pencolor('yellow')
t.goto(0,180)
t.left(60)
t.pendown()
t.forward(15)
t.left(80)
t.forward(7)
t.right(80)
t.forward(17)
t.penup()


# wand
t.home()
t.pensize(3)
t.pencolor(37,50,71)
t.fillcolor(65,88,129)
t.goto(110,-90)
t.pendown()
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(6)
t.left(90)
t.forward(100)
t.left(90)
t.forward(6)
t.end_fill()
t.penup()







