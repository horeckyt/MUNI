from turtle import Turtle, done, delay
from math import sin, sqrt, radians


def series_sum(n):
    if n == 1:
        return 1

    return series_sum(n-1) + n


def sequence(n):
    if n == 0:
        return 5

    return 2*sequence(n-1) - 1


def screwing(n):
    if n == 2:
        print("twist")
        return

    print("twist")
    screwing(n-1)


def list_sum(l):
    if len(l) == 1:
        return l.pop()
    x = l.pop()
    return x + list_sum(l)


def search(n, l, left, right):
    center = (left + right) // 2

    if l[center] == n:
        return True

    if abs(left-right) == 1:
        return False

    if l[center] > n:
        return search(n, l, left, center)

    if l[center] < n:
        return search(n, l, center, right)


def binary_search(n, l):
    left = 0
    right = len(l) - 1
    center = (left + right) // 2

    if l[center] == n:
        return True

    if l[center] > n:
        return search(n, l, left, center)

    if l[center] < n:
        return search(n, l, center, right)


def tree(length):
    if length > 10:
        julie.forward(length)
        julie.left(angle)
        tree(length / (3/2))
        julie.right(2*angle)
        tree(length / (3/2))
        julie.left(angle)
        julie.backward(length)


def squares(length):
    if length > 10:
        for i in range(4):
            julie.forward(length)
            julie.left(90)
        julie.forward(length / 2)
        julie.left(45)
        squares(length / sqrt(2))


def line(length):
    if length > 5:
        line(length / 3)
        julie.left(60)
        line(length / 3)
        julie.right(120)
        line(length / 3)
        julie.left(60)
        line(length / 3)
    else:
        julie.forward(length)
        julie.left(60)
        julie.forward(length)
        julie.right(120)
        julie.forward(length)
        julie.left(60)
        julie.forward(length)


def koch(length):
    for i in range(3):
        line(length)
        julie.right(120)


def sierpinski(length):
    if length > 20:
        sierpinski(length / 2)
        julie.forward(length / 2)
        sierpinski(length / 2)
        julie.forward(length / 2)
        julie.left(120)
        julie.forward(length / 2)
        sierpinski(length / 2)
        julie.forward(length / 2)
        julie.left(120)
        julie.forward(length)
        julie.left(120)

    else:
        for i in range(3):
            julie.forward(length)
            julie.left(120)


def minim(l, left, right):
    if abs(left - right) < 2:
        if l[left] > l[right]:
            return l[right]
        return l[left]

    center = (left + right) // 2

    x = minim(l, left, center)
    y = minim(l, center + 1, right)

    if x > y:
        return y
    return x

def maxim(l, left, right):
    if abs(left - right) < 2:
        if l[left] < l[right]:
            return l[right]
        return l[left]

    center = (left + right) // 2

    x = maxim(l, left, center)
    y = maxim(l, center + 1, right)

    if x < y:
        return y
    return x


def min_max(l):
    x = minim(l, 0, len(l) - 1)
    y = maxim(l, 0, len(l) - 1)
    print(x, y)
#
# julie = Turtle()
# julie.speed(100)
# # julie.left(90)
# julie.width(2)
# delay(0)
# angle = 90
#
# julie.penup()
# julie.setpos(-250, -250)
# julie.pendown()
# squares(500)
#
# input()
# julie.clear()
#
# julie.penup()
# julie.setpos(0, 0)
# julie.pendown()
# julie.right(90)
# tree(200)
# julie.right(90)
# input()
# julie.clear()
#
# julie.penup()
# julie.setpos(-250, 250)
# julie.pendown()
# koch(200)
# input()
# julie.clear()
#
# julie.penup()
# julie.setpos(-250, -250)
# julie.pendown()
# sierpinski(700)
# input()

min_max([8, 4, 3, 5, 9, 8, 5, 7, 6])
