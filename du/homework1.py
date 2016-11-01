# Tomáš Horecký, 456532


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


def hop(n):
    for i in range(1, n+1):
        current = 3 * i
        if current % 9 == 0:
            print("hop", end="")
        elif current % 10 == 5:
            print("hop", end="")
        else:
            print(current, end="")
        if i != n:
            print("", end=", ")


def g_products(n):
    print("\t", end="")

    for i in range(10, n+1):
        print(i, end="\t")
    print()

    for j in range(10, n+1):
        print(j, end="\t")

        for k in range(10, n+1):
            print(j*k, end="\t")

        print()


def tree(n, l):
    for i in range(n):
        for j in range(l):
            for k in range(l-j-1):
                print("  ", end="")
            for m in range(2*j+1):
                print("# ", end="")
            print()


def honey_comb(length):

    bee_turtle = Turtle()
    bee_turtle.speed(5)
    bee_turtle.width(2)

    innerAngle = 120

    for i in range(6):
        for j in range(6):
            bee_turtle.forward(length)
            bee_turtle.left(180 - innerAngle)
        bee_turtle.forward(length)
        bee_turtle.right(180 - innerAngle)

    input("Press enter to continue...")
    bee_turtle.reset()
    bee_turtle.ht()


# Draws a circle sector, determined by given angle and radius
def turtCircle(turt, r, angle):
    dist = (pi * r) / 180
    for i in range(angle):
        turt.forward(dist)
        turt.left(1)


# Draws a flower
def flower():

    flower_turtle = Turtle()
    flower_turtle.speed(0)
    flower_turtle.width(2)
    delay(0)


    petals = 3
    radius = 100
    angle = 90

    """
    # This function can also draw as many petals as you want

    petals = abs(inputInt("How many petals would you like the flower to have? "))
    radius = abs(inputInt("Enter radius of a circle sector (Enter 0 for default radius): "))
    angle = abs(inputInt("Enter angle of a circle sector(Enter 0 for default angle): ") % 181)

    if radius == 0:
        radius = 100
    if angle == 0:
        angle = 90
    """
    stepAngle = 360 / petals

    for l in range(petals):
        turtCircle(flower_turtle, radius, angle)
        flower_turtle.left(180 - angle)
        turtCircle(flower_turtle, radius, angle)
        flower_turtle.right(180 + angle)
        flower_turtle.left(stepAngle)

    flower_turtle.width(3)
    flower_turtle.left(230)
    turtCircle(flower_turtle, 4 * radius, 50)



print("1. hop(n) function: ")
hop(inputInt("How many multiples of 3 would you like to print? "))

print("\n2. g_products(n) function: ")
g_products(inputInt("How large would you like the table to be? (Must be larger than 10) "))

print("\n3. tree(n, l) function: ")
tree(inputInt("How many parts would you like the tree to have? "),
     inputInt("How many lines should each part have? "))

print("\n4. honey_comb(length) function: ")
honey_comb(inputInt("Input the length of the honey comb's side: "))

print("\n5. flower() function: ")
flower()

done()
