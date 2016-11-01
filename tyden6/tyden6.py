from random import randint
from datetime import datetime, time


def inputInt(prompt):

    stringIn = input(prompt)

    try:
        intIn = int(stringIn)
        return intIn
    except ValueError:
        print("Not an integer, try again.")
        return inputInt(prompt)


def guess_human(upper_bound):
    number = randint(1, upper_bound)
    prompt = "I'm thinking of a number between 1 and " + str(upper_bound) + ". Can you guess what it is? "
    guessed_numer = inputInt(prompt)
    while guessed_numer != number:
        if guessed_numer < number:
            guessed_numer = inputInt("The number I'm thinking of is larger. Try again: ")
        else:
            guessed_numer = inputInt("The number I'm thinking of is smaller. Try again: ")
    print("That's right!")


def guess_pc(upper_limit):
    left = 0
    right = upper_limit
    answer = 1
    print("Think of a number between 1 and", upper_limit, "and I'll try to guess what it is.")
    while answer != 0:
        guessed_number = (right+left)//2 + 1
        print("I guess", guessed_number)
        print("(0) correct")
        print("(1) guessed number is smaller than the one you're thinking of")
        print("(2) guessed number is larger than the one you're thinking of")
        answer = inputInt("Answer: ")
        if answer == 0:
            print("Woo!")
        if answer == 1:
            right = guessed_number
        if answer == 2:
            left = guessed_number


def guess_pc_pc(upper_limit):
    number = randint(1, upper_limit)
    left = 0
    right = upper_limit
    guessed_number = (right + left) // 2
    tries = 0

    while guessed_number != number:
        if guessed_number < number:
            left = guessed_number
        else:
            right = guessed_number
        guessed_number = (right + left) // 2
        tries += 1

    print("The number was", number, "and it took ", tries, "guesses to guess.")


def binary_search(needle, haystack):
    left = 0
    right = len(haystack)
    pivot = (left + right) // 2

    while haystack[pivot] != needle and left != pivot and right != pivot:
        if haystack[pivot] < needle:
            left = pivot
        else:
            right = pivot
        pivot = (left + right) // 2


    if haystack[pivot] == needle:
        return True
    else:
        return False


def binary_search_position(needle, haystack):
    left = 0
    right = len(haystack)
    pivot = (left + right) // 2

    while haystack[pivot] != needle and left != pivot and right != pivot:
        if haystack[pivot] < needle:
            left = pivot
        else:
            right = pivot
        pivot = (left + right) // 2


    if haystack[pivot] == needle:
        return pivot
    else:
        return -1


def find_left(needle, haystack):
    left = 0
    right = len(haystack)
    pivot = (left + right) // 2
    index = 0

    if haystack[left] == needle:
        return left

    while left != pivot and right != pivot:
        if haystack[pivot] == needle:
            if index == 0 or index > pivot:
                index = pivot
            right = pivot
        elif haystack[pivot] > needle:
            right = pivot
        else:
            left = pivot
        pivot = (left + right) // 2

    if haystack[index] == needle:
        return index
    else:
        return -1


def find_right(needle, haystack):
    left = 0
    right = len(haystack)
    pivot = (left + right) // 2
    index = 0

    if haystack[right-1] == needle:
        return right -1

    while left != pivot and right != pivot:
        if haystack[pivot] == needle:
            if index == 0 or index < pivot:
                index = pivot
            left = pivot
        elif haystack[pivot] > needle:
            right = pivot
        else:
            left = pivot
        pivot = (left + right) // 2

    if haystack[index] == needle:
        return index
    else:
        return -1


def binary_search_position_list(needle, haystack):
    most_left_index = find_left(needle, haystack)
    most_right_index = find_right(needle, haystack)
    if most_left_index == -1 or most_right_index == -1:
        return []

    indexes = list(range(most_left_index, most_right_index +1))

    return indexes


def super_power(base, exp):
    start = datetime.now()
    curr_power = 1
    result = base
    count = 0
    powers = {1: base}
    while curr_power < exp:
        if curr_power*2 < exp:

            curr_power *= 2
            result **= 2

            tmp_power = curr_power
        else:
            tmp_power
            while curr_power+tmp_power > exp:
                tmp_power //= 2
            curr_power += tmp_power
            result *= powers[tmp_power]

        print (curr_power)
        powers[curr_power] = result
        count += 1

    print("Time: ", datetime.now()-start)
    print(result, ' ', count)
    print(powers)


def power(base, exp):
    start = time.now()
    curr_power = 1
    result = base
    count = 1
    while curr_power < exp:
        curr_power += 1
        result *= base
        count += 1

    print("Time: ", time.now()-start)
    print(result, ' ', count)


# print(binary_search(2, [1, 2, 5, 8]))
# print(binary_search_position(2, [1, 2, 5, 8]))
# print(binary_search_position_list(5, [1, 2, 3, 5, 5, 5, 5, 8]))

super_power(2, 100)
power(2,100)