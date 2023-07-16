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

def get_computer_input(board):
    available_moves = []
    for i in range(9):
        if board[i] == " ":
            available_moves.append(i)
    return random.choice(available_moves)

def main():
    board = [" "] * 9
    player = "X"
    while True:
        draw_board(board)
        if player == "X":
            move = get_player_input()
            while board[move - 1] != " ":
                print("Invalid move. Please try again.")
                move = get_player_input()
        else:
            move = get_computer_input(board)
        board[move - 1] = player
        if check_winner(board):
            draw_board(board)
            print(player, "wins!")
            break
        if " " not in board:
            draw_board(board)
            print("It's a draw!")
            break
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()
