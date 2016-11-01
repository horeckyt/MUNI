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


# Prints all odd divisors of integer n
def oddDiv(n):

    print("Odd divisors of ", n, ":")
    n = abs(n)
    for i in range(1, n//2):
        if (n % i == 0) and (i % 2 == 1):
            print(i, end=" ")

    if (n % 2 == 1):
        print(n)


# Recursive part of Tribonacci series
def TribonacciRec(n, i, a, b, c):
    d = a + b + c
    print(d, end="")
    i += 1
    if i <= n:
        print(", ", end="")
        TribonacciRec(n, i, b, c, d)


# Prints first 3 numbers of Tribonacci series and starts the recursive part above
def Tribonacci(n):
    a = 0
    b = 1
    c = 1
    i = 4
    print("{}, {}, {}, ".format(a, b, c), end="")
    TribonacciRec(n, i, a, b, c)


# Prints a table of reminders
def remainders(n):

    print("", end="\t")
    for i in range(1, n+1):
        print(i, end="\t")

    print("\n", end="\t")
    for i in range(1, n+1):
        print("-", end="\t")
    print()

    for j in range(1, n+1):
        print(j,"|",end="\t")

        for k in range(1,n+1):
            print(j % k, end="\t")
        print()


# Prints a pyramid
def pyramid(n):

    for i in range(n-1):
        for j in range(n-i, 0,-1):
            print(" ", end=" ")
        print("#", end=" ")

        for k in range(2*i - 1, 0, -1):
            print(".", end=" ")

        if i != 0:
            print("#",end="\n")
        else:
            print()

    print(" ",end=" ")

    for l in range(2*n-1):
        print("#", end=" ")


# Draws a circle sector, determined by given angle and radius
def turtCircle(turt, r, angle):
    dist = (pi * r) / 180
    for i in range(angle):
        turt.forward(dist)
        turt.left(1)


# Draws a flower
def flower():

    petals = abs(inputInt("How many petals would you like the flower to have? "))
    radius = abs(inputInt("Enter radius of a circle sector (Enter 0 for default radius): "))
    angle = abs(inputInt("Enter angle of a circle sector(Enter 0 for default angle): ") % 181)

    if radius == 0:
        radius = 100
    if angle == 0:
        angle = 90

    t = Turtle()
    t.speed(100)
    t.width(2)
    t.ht()
    delay(0)
    stepAngle = 360 / petals

    for l in range(petals):
        turtCircle(t, radius, angle)
        t.left(180 - angle)
        turtCircle(t, radius, angle)
        t.right(180 + angle)
        t.left(stepAngle)
    done()

"""
print("Finding odd divisors of a number")
oddDiv(inputInt("Input an integer: "))

print("\nPrinting Tribonacci sequence")
Tribonacci(inputInt("How many Tribonacci numbers would you like to print? "))

print("\nPrinting a table of remainders")
remainders(inputInt("Input an integer: "))

print("\nPrinting a pyramid")
pyramid(inputInt("Input an integer: "))

print("\nDrawing a flower")
flower()
"""
pyramid(inputInt("Input an integer: "))
