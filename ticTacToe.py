# returns the array representation of an empty board
def new_board():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# places color (X/O) in position x, y
def move(pos, color):
    board[pos[0]][pos[1]] = color


# deletes move in position x, y
def delete_move(pos):
    board[pos[0]][pos[1]] = " "


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


# checks all possibilities and returns the best place for O to go - currently unfinished
def best_move(color, init):
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if not taken((i, j)):
                move((i, j), color)
                moved = (i, j)
                if win():
                    if color == "O":
                        possible_moves.append(("win", 1), moved)  # 1/1 wins
                    else:
                        possible_moves.append(("lose", 0), moved)  # 0/1 wins
                else:
                    if full():
                        possible_moves.append(("tie", 0), moved)  # 0/1 wins
                    else:
                        if color == "O":
                            possible_moves.append(best_move("X", False), moved)
                        else:
                            possible_moves.append(best_move("O", False), moved)
                delete_move(moved)
    if color == "O":
        best = ("lose", 0)
        for i in possible_moves:
            if i[0][0] == "win":
                if init:
                    return i[1]
                return i[0]
            if i[0][0] == "tie":
                if best[0] == "lose":
                    best = i[0]
                else:
                    if i[0][1] > best[1]:
                        best = i[0]


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
        move(best_move(turn, True), turn)
        turn = "X"
    print_board()
if win():
    if turn == "O":
        print("You win!")
    else:
        print("You lose!")
else:
    print("It's a tie.")
