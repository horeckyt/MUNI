from collections import deque
from random import randint

def to_morse(text):
    t = text.upper()
    trans = ""
    for c in t:
        if c in morse_dict.keys():
            trans += morse_dict[c]  + " / "
        else:
            trans += c
    return trans


def freq_analysis(text):
    t = text.lower()
    words = t.split()
    word_dict = {}
    for w in words:
        word_dict[w] = words.count(w)

    # print(word_dict.sort())
    word_keys = list(word_dict.keys())
    word_keys.sort()
    for k in word_keys:
        print(k + ":", word_dict[k])
    print()


def sudoku_line_check(l):
    line_set = set(l)
    if len(line_set) != 9:
        return False
    for i in line_set:
        if i > 9 or i < 1:
            return False
    return True


def hot_potato(namelist, k):
    players = deque(namelist)
    print("These are the players: " + ", ".join(players))
    for i in range(len(namelist)-1):
        print("Round", i+1)
        rand = randint(1, len(players))
        for j in range(rand-1):
            players.append(players.popleft())
        print("Random roll:", rand)
        print(players.popleft() + " is out!")
        print("Players left: " + ", ".join(players))
    print(players.pop() + " wins!")



morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.',
                  '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
morse_dict = {}
i = 0
for m in morse_code:
    morse_dict[chr(ord("A")+i)] = m
    i += 1
morse_dict[" "] = " | "

print(to_morse("Hello World!"))
print()

freq_analysis("Monty Python and Monty Python all over here.")

print(sudoku_line_check([1, 2, 8, 9, 3, 5, 6, 7, 4])) # True
print(sudoku_line_check([1, 2, 8, 9, 3, 5, 7, 4])) # False
print(sudoku_line_check([1, 1, 2, 8, 9, 3, 5, 7, 4])) # False
print(sudoku_line_check([0, 1, 2, 3, 4, 5, 6, 7, 8])) # False
print()

hot_potato(["Bill","David","Susan","Jane","Kent","Brad","Sam"],7)