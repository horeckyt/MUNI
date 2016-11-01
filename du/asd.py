from turtle import Turtle, done, delay
from math import pi


# Checks if input is an integer
def inputInt(prompt):

    stringIn = input(prompt)

    try:
        intIn = int(stringIn)
        return intIn
    except ValueError:
        print("Not an integer, try again.")
        return inputInt(prompt)


def honey_comb(length):

    innerAngle = 120
    t = Turtle()
    for i in range(6):
        for j in range(6):
            t.forward(length)
            t.left(180 - innerAngle)
        t.forward(length)
        t.right(180 - innerAngle)

    input()
    t.reset()
    t.ht()


# Draws a circle sector, determined by given angle and radius
def turtCircle(turt, r, angle):
    dist = (pi * r) / 180
    for i in range(angle):
        turt.forward(dist)
        turt.left(1)


# Draws a flower
def flower():
    turt = Turtle()
    turt.width(2)
    delay(0)
    petals = 3
    radius = 100
    angle = 90


    # This function can also draw as many petals as you want

    petals = abs(inputInt("How many petals would you like the flower to have? "))
    radius = abs(inputInt("Enter radius of a circle sector (Enter 0 for default radius): "))
    angle = abs(inputInt("Enter angle of a circle sector(Enter 0 for default angle): ") % 181)

    if radius == 0:
        radius = 100
    if angle == 0:
        angle = 90

    stepAngle = 360 / petals

    for l in range(petals):
        turtCircle(turt, radius, angle)
        turt.left(180 - angle)
        turtCircle(turt, radius, angle)
        turt.right(180 + angle)
        turt.left(stepAngle)

    turt.width(3)
    turt.left(230)
    turtCircle(turt, 2 * radius, 80)

    done()



flower()
