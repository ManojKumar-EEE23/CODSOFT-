import math

# Board symbols
HUMAN = "X"
AI = "O"
EMPTY = " "

# Initialize the board
def create_board():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if a move is valid
def is_valid_move(board, row, col):
    return board[row][col] == EMPTY

# Make a move on the board
def make_move(board, row, col, player):
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False

# Check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

# Check if the game is a draw
def is_draw(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

# Minimax algorithm with optional Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    winner = check_winner(board)
    if winner == AI:
        return 1
    if winner == HUMAN:
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = AI
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = HUMAN
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Find the best move for the AI
def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = AI
                score = minimax(board, 0, False)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

# Main game loop
def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human player's turn
        row, col = map(int, input("Enter your move (row and column: 0, 1, or 2): ").split())
        if make_move(board, row, col, HUMAN):
            print_board(board)
            if check_winner(board):
                print("You win!")
                break
            if is_draw(board):
                print("It's a draw!")
                break

            # AI's turn
            print("AI is making a move...")
            ai_move = find_best_move(board)
            make_move(board, ai_move[0], ai_move[1], AI)
            print_board(board)

            if check_winner(board):
                print("AI wins!")
                break
            if is_draw(board):
                print("It's a draw!")
                break
        else:
            print("Invalid move. Try again!")

if __name__ == "__main__":
    play_game()
