# Tomáš Horecký, 456532

from random import randint


def print_board(mat, mat_thr, pat, pat_thr, length):
    print("Mat: ", end="")
    for i in mat_thr:
        print(i, end=", ")
    print("Pat: ", end="")
    for j in pat_thr:
        print(j, end=", ")
    print()

    print("home", end=" ")
    for k in range(length):
        if k == mat-1:
            print("M", end=" ")
        else:
            print(".", end=" ")
    print("finish")
    print("home", end=" ")
    for l in range(length):
        if l == pat-1:
            print("P", end=" ")
        else:
            print(".", end=" ")
    print("finish")
    print()


def throws():
    throw = randint(1, 6)
    thr = [throw]

    while throw == 6:
        throw = randint(1, 6)
        thr.append(throw)

    return thr


def pix(length, leg, print_games):

    pat_pos = 0
    mat_pos = 0

    for i in range(leg):
        if print_games:
            print("Round", i+1)

        throws_mat = throws()

        for j in throws_mat:
            if j <= length - mat_pos:
                mat_pos += j

        if mat_pos == pat_pos:
            pat_pos = 1

        throws_pat = throws()

        for k in throws_pat:
            if k <= length - pat_pos:
                pat_pos += k

        if pat_pos == mat_pos:
            mat_pos = 1

        if mat_pos == length:
            if print_games:
                print_board(mat_pos, throws_mat, pat_pos, throws_pat, length)
                print("Mat wins!")
            return "mat"

        if pat_pos == length:
            if print_games:
                print_board(mat_pos, throws_mat, pat_pos, throws_pat, length)
                print("Pat wins!")
            return "pat"

        if print_games:
            print_board(mat_pos, throws_mat, pat_pos, throws_pat, length)

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
    print("Games won by Mat: ", mat_wins, " ({0:.01%})".format(mat_wins/count))
    print("Games won by Pat: ", pat_wins, " ({0:.01%})".format(pat_wins/count))
    print("Games that ended in a draw: ", draws, " ({0:.01%})".format(draws/count))


pix_analyze(20, 12, 500, False)
