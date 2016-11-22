# Tomáš Horecký, 456532

from random import randint


# Checks if input is an integer
def input_int(prompt):
    string_in = input(prompt)
    try:
        int_in = int(string_in)
        return int_in
    except ValueError:
        print("Not an integer, try again:")
        return input_int(prompt)


def print_board(b):
    print(" ", end="")
    for i in b:
        print(i, end="  ")
    print()
    for j in range(len(b)):
        print("{:2}".format(j+1), end=" ")
    print()


# Checks whether if there are 3 consecutive Xs on the board
def is_game_over(b):
    for i in range(len(b)-2):
        if b[i] == b[i+1] == b[i+2] == "X":
            return True
    return False


# Taking input from player, validating it, and checking if the move player made is winning
# if not, calls computer to play
def player_move(b, taken):
    print("Playing: Player")
    x = input_int("Choose a position: ") - 1
    while x < 0 or x > len(b) - 1 or b[x] == "X":
        x = input_int("Invalid choice, please try again: ") - 1
    b[x] = "X"
    taken.append(x)
    print("Position:", x + 1)
    print_board(b)
    print()
    if is_game_over(b):
        print("Player Wins!")
    else:
        computer_move(b, taken)


# Looks for a move that would win the game ("X _ X" or "_ X X _"  , if there isn't one, returns -1
def find_winning(b, taken):
    winning_pos = -1
    for i in range(len(b)-1):
        if i-1 in taken and i+1 in taken:
            winning_pos = i
        elif b[i] == "X" and b[i+1] == "X":
            if i-1 not in taken and i-1 >= 0:
                winning_pos = i - 1
            elif i+2 <= len(b):
                winning_pos = i + 2

    return winning_pos


# Looks for a move that would not allow the player to win the game on his next move (looks for combinations
# with no taken positions in range of 2 ("_ _ i _ _")
# if there isn't one, returns -1
def find_first_safe(n, taken):
    for i in range(n):
        checking = [j for j in range(i-2, i+3)]
        is_safe = True
        # print(checking)
        for k in checking:
            if k in taken:
                is_safe = False
        if is_safe:
            return i
    return -1


# Computer choosing a position
def computer_make_move(b, taken, name):
    x = find_winning(b, taken)

    if x == -1:
        x = find_first_safe(len(b), taken)
        # if there are no winning or safe moves, chooses a random position that is not taken
        if x == -1:
            x = randint(0, len(b))
            while x in taken:
                x = randint(0, len(b))

    b[x] = "X"
    taken.append(x)
    print("Playing: " + name)
    print("Position:", x + 1)
    print_board(b)
    print()


# A function used in Computer vs Player mode
def computer_move(b, taken):
    computer_make_move(b, taken, "Computer")
    if is_game_over(b):
        print("Computer Wins!")
    else:
        player_move(b, taken)


# Next 2 functions are used in Computer vs Computer mode
# Since the board size doesn't change and both Computers have a given set of rules they follow,
# the outcome of the game is determined by who makes the first move, which is random
def computer1(b, taken, name):
    computer_make_move(b, taken, "Computer1")
    if is_game_over(b):
        print(name + " Wins!")
    else:
        computer2(b, taken, "Computer2")


def computer2(b, taken, name):
    computer_make_move(b, taken, "Computer2")
    if is_game_over(b):
        print(name + " Wins!")
    else:
        computer1(b, taken, "Computer1")


# Sets up the board, calls the first player
def tic_tac_toe(board_size, first_player, mode):
    if first_player == 0:
        first_player = randint(1, 2)

    board = ["_" for _ in range(board_size)]
    taken_positions = []
    print_board(board)
    print()
    if mode == 0:
        if first_player == 1:
            player_move(board, taken_positions)
        else:
            computer_move(board, taken_positions)
    else:
        if first_player == 1:
            computer1(board, taken_positions, "Computer2")
        else:
            computer2(board, taken_positions, "Computer1")


# Starting the game and displaying some basic information
def game_init():
    print("Tic-tac-toe")
    print("Choose mode:")
    print("0. Computer vs Player")
    print("1. Computer vs Computer")
    mode = input_int("Mode: ")
    while mode not in [0, 1]:
        print("Invalid choice, please try again:")
        mode = input_int("")

    if mode == 0:
        print("Who will start the game?")
        print("0. Random \n1. You \n2. Computer ")
        player = input_int("Choose a player: ")

        while player not in [0, 1, 2]:
            print("Invalid choice, please try again:")
            player = input_int("")
    else:
        player = 0
    tic_tac_toe(26, player, mode)


game_init()
