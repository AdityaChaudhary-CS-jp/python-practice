# Problem281
from turtle import *
a = Turtle()
b = int(input('Enter the radius ='))
while b!=100:
    a.penup()
    a.goto(0,-b)
    a.pendown()
    a.fillcolor('blue')
    a.begin_fill()
    a.circle(b)
    a.end_fill()
    b=b+20
    if b>=200:
       break
