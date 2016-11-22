from time import clock


def triangle(n):
    l = []
    tmp = []
    for i in range(n+1):
        for j in range(i):
            tmp.append(1)
        if len(tmp) > 0:
            l.append(tmp)
        tmp = []
    return l

"""
def merge(array):
    if len(array) == 1:
        return
    left = 0
    right = len(array)-1
    center = (left + right) // 2
    left_i = left
    right_i = center + 1

    while left_i <= center and right_i <= right:
        if array[left_i] < array[right_i]:
            left_i += 1
        else:
            array[left_i], array[right_i] = array[right_i], array[left_i]
            right_i += 1

    if right_i <= right:
        for k in array[right_i:right+1]:
            dupe.append(k)
    elif left_i <= center:
        for k in array[left_i:center+1]:
            dupe.append(k)


def mergesort(array):
    left = 0
    right = len(array)
    center = (left + right) // 2

    if left == right:
        return
    dupe = array[:]

    mergesort(array[left:center])
    dupe = array[:center+1] + dupe[center+1:]
    mergesort(array[center+1:right])
    dupe = dupe[:center+1] + array [center + 1:]
    merge(dupe)
    array = dupe[:]
"""


def bubble(a):
    array = a[:]
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j + 1], array[j]
    return array


def findmin(a, left):
    min = a[left]
    min_i = left
    for i in range(left, len(a)):
        if a[i] < min:
            min = a[i]
            min_i = i
    return min_i


def select(a):
    array = a[:]
    for i in range(len(array) - 1):
        min_i = findmin(array, i)
        if array[i] > array[min_i]:
            array[i], array[min_i] = array[min_i], array[i]
    return array


def insert(a):
    array = a[:]
    for i in range(len(array) - 1):
        j = i + 1
        tmp = array[j]
        while j > 0 and tmp < array[j-1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = tmp
    return array


def quick(array):
    if len(array) < 2:
        return array
    a = array[:]

    pivot = (0 + len(a)) // 2
    smaller = []
    larger = []

    for i in range(len(a)):
        if i != pivot:
            if a[i] > a[pivot]:
                larger.append(a[i])
            else:
                smaller.append(a[i])

    smaller_sorted = quick(smaller)
    larger_sorted = quick(larger)
    smaller_sorted.append(a[pivot])
    a = smaller_sorted + larger_sorted
    return a

def elapsed(func, l):

    now = clock()
    a = func(l)
    el = clock() - now
    print(func.__name__, "sort: {0:.000001} ms,\t".format(el), "result:", a)

l = [7, 6, 100, 3, 2, 11, -1, 10, 10, 42, 42, 42, 2, 13, 0, -5]


elapsed(bubble, l)
elapsed(select, l)
elapsed(insert, l)
elapsed(sorted, l)
elapsed(quick, l)
# print(l)
