# returns the array representation of an empty board
def new_board():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# places color (X/O) in position x, y
def move(pos, color):
    board[pos[0]][pos[1]] = color


# prints the current board state
def print_board():
    board_str = "+ - - - +\n"
    for i in range(3):
        board_str += "| "
        for j in range(3):
            board_str += str(board[i][j]) + " "
        board_str += "|\n"
    board_str += "+ - - - +"
    print(board_str)


# returns true if either color (X/O) has won
def win():
    for i in range(3):
        if board[i][0] != " " and board[i][0] == board[i][1] == board[i][2]:
            return True
        if board[0][i] != " " and board[0][i] == board[1][i] == board[2][i]:
            return True
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True
    return False


# returns true if the board is full
def full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True


# checks all possibilities and returns the best place for X to go - currently unfinished
def best_move():
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return i, j


# checks to see if the position is taken
def taken(pos):
    if board[pos[0]][pos[1]] == " ":
        return False
    return True


# prompts the user where they want to move, keeps asking until a valid position is chosen
def prompt_move():
    answer = ""
    while True:
        if len(answer) == 3:
            if answer[1] == ",":
                if answer[0] == "1" or answer[0] == "2" or answer[0] == "3":
                    if answer[2] == "1" or answer[2] == "2" or answer[2] == "3":  # valid position
                        pos = int(answer[2]) - 1, int(answer[0]) - 1
                        if not taken(pos):
                            break
                        else:
                            print("That position is taken.")
        answer = input("What position would you like to move? ie \"1,2\": ")
    return pos


board = new_board()
print_board()
turn = ""
while turn != "1" and turn != "2":
    turn = input("Would you like to go 1st or 2nd? (1 / 2): ")  # user is X, computer is O
if turn == "1":
    turn = "X"
else:
    turn = "O"

while not full() and not win():
    if turn == "X":  # your turn
        move(prompt_move(), turn)
        turn = "O"

    else:  # computer's turn
        move(best_move(), turn)
        turn = "X"
    print_board()
if win():
    if turn == "O":
        print("You win!")
    else:
        print("You lose!")
else:
    print("It's a tie.")
