import random

def draw_board(board):
    print("-------------")
    for row in board:
        print("| " + " ".join(row) + " |")
    print("-------------")

def get_player_input():
    while True:
        player_input = input("Enter your move (1-9): ")
        try:
            player_input = int(player_input)
            if 1 <= player_input <= 9:
                return player_input
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_winner(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            return board[row][0]
        if board[0][row] == board[1][row] == board[2][row] != " ":
            return board[0][row]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def get_computer_input(board):
    available_moves = [i + 1 for i, val in enumerate(board) if val == " "]
    return random.choice(available_moves)

def main():
    board = [" "] * 9
    player = "X"
    while True:
        draw_board(board)
        if player == "X":
            move = get_player_input()
        else:
            move = get_computer_input(board)

        if board[move - 1] == " ":
            board[move - 1] = player
        else:
            print("Invalid move. Please try again.")
            continue

        winner = check_winner(board)
        if winner:
            draw_board(board)
            print(f"{winner} wins!")
            break

        if " " not in board:
            draw_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()
