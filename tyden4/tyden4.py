from random import random, randint
from math import sqrt

def dice():
    return randint(1, 6)


def turn():
    throwSum = 0
    rand = randint(1, 6)
    while rand % 2 == 0:
        throwSum += rand
        rand = randint(1, 6)
    throwSum += rand
    return throwSum


def dice_min_max(count, lower, upper):
    throws = []
    for i in range(count):
        throws.append(randint(lower, upper))

    print("Max: ", max(throws))
    print("Min: ", min(throws))
    print("Average: ", sum(throws)/count)


def dice_freq(count):
    throws = []
    for i in range(count):
        throws.append(randint(1, 6))

    for j in range(1, 7):
        print("Occurrences of ", j, ":", throws.count(j))


def two_dice_freq(count):
    throws = []
    for i in range(count):
        dice_one = randint(1, 6)
        dice_two = randint(1, 6)
        throws.append(dice_one + dice_two)

    for j in range(1, 13):
        print("Occurrences of ", j, ":", throws.count(j))


def coin_flip():
    rand = randint(1, 100)
    if rand <= 85:
        return True
    else:
        return False


def drunkman_simulator(dist, steps, output):
    drunk_pos = dist//2
    drunk_steps = 0
    directions = [-1, 1]
    while 0 < drunk_pos < dist+1 and drunk_steps < steps:
        if output:
            print("home", end=" ")
            for j in range(1, dist+1):
                if j == drunk_pos:
                    print("*", end=" ")
                else:
                    print(".",  end=" ")
            print("pub")

        drunk_pos += directions[randint(0, 1)]
        drunk_steps += 1

    if drunk_pos == 0:
        return True
    else:
        return False
    """
    elif drunk_pos == dist+1:
        print("Ended up in the pub")
    else:
        print("He fell asleep")
    """


def drunkman_analysis(size, steps, count):
    stats = []

    for i in range(count):
        stats.append(drunkman_simulator(size, steps, False))

    got_home = stats.count(True)

    print("Got home safely in ", (got_home/count) * 100, "% of cases")


def check_bounds(x, width):
    if x < 0:
        x = 0
    elif x > width - 1:
        x = width - 1
    return x


def printfield(x, y, f, w):
    for i in range(w):
        for j in range(w):
            if i == x and y == j:
                print("Hunter", end="\t")
            else:
                print(f[i][j], end="\t")
        print()
    print()


def treasure_hunter(width, steps):
    field = [[False for x in range(width)] for y in range(width)]
    field[randint(0, width-1)][randint(0, width-1)] = True
    hunter_x = 0
    hunter_y = 0

    i = 0

    while not(field[hunter_x][hunter_y]) and i < steps:
        rand = randint(0, 3)
        if rand == 0:
            hunter_x += 1
        if rand == 1:
            hunter_y -= 1
        if rand == 2:
            hunter_x -= 1
        if rand == 3:
            hunter_y += 1

        i += 1

        hunter_x = check_bounds(hunter_x, width)
        hunter_y = check_bounds(hunter_y, width)

        printfield(hunter_x, hunter_y, field, width)

    return field[hunter_x][hunter_y]


def treasure_hunter_analysis(width, steps, count):
    stats = []

    for i in range(count):
        stats.append(treasure_hunter(width, steps))

    treasure_found = stats.count(True)

    print("Treasure found in ", 100* treasure_found/count, "% of cases")


def tramway_waiting_more_than(w, n, count):
    waited_more = 0
    for i in range(count):
        tram_arrival = n - n*random()
        if tram_arrival > w:
            waited_more += 1

    print("Waited more than", w, "minutes in ", 100*waited_more/count, "% of cases")


def random_point_distance(size):
    x = [randint(0, size-1), randint(0, size-1)]
    y = [randint(0, size-1), randint(0, size-1)]

    dist = sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
    return dist


def average_points_distance(count, size):
    stats = []
    for i in range(count):
        stats.append(random_point_distance(size))
    print("Avg. distance: ", sum(stats)/count)


def random_student(n, count):
    for i in range(count):
        for j in range(n//2):
            pass

treasure_hunter(5,100)