from turtle import Turtle, done
from math import pi

# Draws a circle sector, determined by given angle and radius
def turtCircle(r, angle):
    dist = (pi * r)/180
    for i in range(angle):
        t.forward(dist)
        t.left(1)

# Draws a flower
def flower(petals, r, angle):
    stepAngle = 360 // petals
    for l in range(petals):
        turtCircle(r, angle)
        t.left(180-angle)
        turtCircle(r, angle)
        t.right(180+angle)
        t.left(stepAngle)


t = Turtle()
t.speed(0)
t.width(2)
flower(4, 100, 90)
done()