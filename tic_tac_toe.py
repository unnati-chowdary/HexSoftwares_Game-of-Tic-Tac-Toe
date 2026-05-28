import random
board = [" " for _ in range(9)]
def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--|---|--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--|---|--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5],[6,7,8],
        [0,3,6], [1,4,7],[2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
def check_draw():
    return " " not in board
def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Position already taken!")

        except:
            print("Invalid input!")
def computer_move():
    empty_positions = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty_positions)
    board[move] = "O"
print("Welcome to Tic-Tac-Toe!")
display_board()
while True:
    player_move()
    display_board()
    if check_winner("X"):
        print("Congratulations! You win!")
        break
    if check_draw():
        print("It's a draw!")
        break
    print("Computer's turn...")
    computer_move()
    display_board()
    if check_winner("O"):
        print("Computer wins!")
        break
    if check_draw():
        print("It's a draw!")
        break
