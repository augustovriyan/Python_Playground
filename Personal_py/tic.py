import random

def draw_board(board):
    """Display the current state of the Tic-Tac-Toe board."""
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def get_player_input():
    """Get valid player move input."""
    while True:
        try:
            player_input = int(input("Enter your move (1-9): "))
            if 1 <= player_input <= 9:
                return player_input
            print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_winner(board):
    """Check if there's a winner on the board."""
    for row in board:
        if all(cell == row[0] and cell != " " for cell in row):
            return row[0]

    for col in range(3):
        if all(row[col] == board[0][col] and board[0][col] != " " for row in board):
            return board[0][col]

    if all(board[i][i] == board[0][0] and board[i][i] != " " for i in range(3)):
        return board[0][0]

    if all(board[i][2 - i] == board[0][2] and board[i][2 - i] != " " for i in range(3)):
        return board[0][2]

    return None

def get_computer_input(board):
    """Generate computer's move."""
    available_moves = [str(i + 1) for i, cell in enumerate(board) if cell == " "]
    return random.choice(available_moves)

def main():
    """Main game loop."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        draw_board(board)

        if current_player == "X":
            move = get_player_input()
        else:
            move = get_computer_input(board)

        row, col = divmod(move - 1, 3)

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move. Please try again.")
            continue

        winner = check_winner(board)
        if winner:
            draw_board(board)
            print(f"{winner} wins!")
            break

        if all(cell != " " for row in board for cell in row):
            draw_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
