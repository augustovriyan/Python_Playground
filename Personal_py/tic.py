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
            player_input = str(player_input)
            if player_input in range(1, 10):
                return player_input
        except ValueError:
            pass

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

def main():
    board = [" "] * 9
    player = "X"
    while True:
        draw_board(board)
        move = get_player_input()
        board[int(move) - 1] = player
        if check_winner(board):
            print(player, "wins!")
            break
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()
