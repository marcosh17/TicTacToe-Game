import random

def print_board(board):
    print("\n")
    print("\t     |     |")
    print(f"\t  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}")
    print("\t     |     |")
    print("\n")

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def has_empty_spaces(board):
    for row in board:
        if " " in row:
            return True
    return False

def player_move(board):
    while True:
        try:
            row = int(input("Choose a row (1-3): ")) - 1
            col = int(input("Choose a column (1-3): ")) - 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("That cell is not valid or is already occupied. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def ai_move(board, difficulty):
    if difficulty == "easy":
        return random_move(board)
    elif difficulty == "medium":
        return medium_move(board)
    else:
        move = minimax_move(board, "O")
        return move

def random_move(board):
    empty_spaces = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_spaces)

def medium_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if check_winner(board, "X"):
                    board[i][j] = "O"
                    return i, j
                board[i][j] = " "
    return random_move(board)

def minimax_move(board, player):
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif not has_empty_spaces(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                return "easy"
            elif choice == 2:
                return "medium"
            elif choice == 3:
                return "hard"
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")

def tic_tac_toe_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    difficulty_level = choose_difficulty()

    while True:
        print_board(board)
        if current_player == "X":
            player_move(board)
        else:
            row, col = ai_move(board, difficulty_level)
            board[row][col] = "O"

        if check_winner(board, current_player):
            print(f"Player {current_player} has won!")
            break
        if not has_empty_spaces(board):
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe_game()
