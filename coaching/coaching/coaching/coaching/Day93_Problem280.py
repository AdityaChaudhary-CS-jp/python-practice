# Problem280
from turtle import *
a = Turtle()
b = int(input('Enter the radius ='))
while b!=100:
    a.circle(b)
    a.circle(-(b))
    b=b+10
