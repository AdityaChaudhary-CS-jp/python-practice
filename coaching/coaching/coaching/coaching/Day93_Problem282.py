# Problem282
from turtle import *
a = Turtle()
a.penup()
a.goto(-100,20)
a.pendown()
for i in range(4):
    a.backward(50)
    a.right(90)
a.penup()
a.goto(100,20)
a.pendown()
for i in range(4):
    a.backward(50)
    a.right(90)
a.penup()
a.goto(-100,-20)
a.pendown()
for i in range(4):
    a.backward(50)
    a.left(90)
a.penup()
a.goto(100,-20)
a.pendown()
for i in range(4):
    a.backward(50)
    a.left(90)
