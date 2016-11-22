# Tomáš Horecký, 456532

from random import randint


class Player:
    def __init__(self, name):
        self.position = 0
        self.thr = []
        self.name = name

    def reset_pos(self):
        self.position = 0

    def reset_thr(self):
        self.thr = []

    def move(self, length):
        throw = randint(1, 6)
        self.thr = [throw]

        while throw == 6:
            throw = randint(1, 6)
            self.thr.append(throw)

        for k in self.thr:
            if k <= length - self.position:
                self.position += k

    def print_board(self, length):
        print(self.name, end=": ")

        for i in self.thr:
            print(i, end=", ")
        print("\nhome", end=" ")

        for k in range(length):
            if k == self.position - 1:
                print(self.name[0], end=" ")
            else:
                print(".", end=" ")

        print("finish")
        self.reset_thr()


def pix(length, leg, print_games):

    mat = Player("Mat")
    pat = Player("Pat")

    for i in range(leg):
        if print_games:
            print("Round", i+1)

        mat.move(length)
        if mat.position == pat.position:
            pat.reset_pos()

        pat.move(length)
        if pat.position == mat.position:
            mat.reset_pos()

        if mat.position == length:
            if print_games:
                mat.print_board(length)
                pat.print_board(length)
                print("Mat wins!")
            return "mat"

        if pat.position == length:
            if print_games:
                mat.print_board(length)
                pat.print_board(length)
                print("Pat wins!")
            return "pat"

        if print_games:
            mat.print_board(length)
            pat.print_board(length)

    if print_games:
        print("It's a draw!")
    return "draw"


def pix_analyze(length, leg, count, print_games):
    results = []
    for i in range(count):
        if print_games:
            print("Game ", i+1)
        results.append(pix(length, leg, print_games))
    mat_wins = results.count("mat")
    pat_wins = results.count("pat")
    draws = results.count("draw")

    print()
    print("Stats: ")
    print("Total games: ", count)
    print("Games won by Mat: ", mat_wins, " ({0:.2%})".format(mat_wins/count))
    print("Games won by Pat: ", pat_wins, " ({0:.2%})".format(pat_wins/count))
    print("Games that ended in a draw: ", draws, " ({0:.2%})".format(draws/count))


pix_analyze(20, 12, 500, False)
# pix(20, 12, True)
