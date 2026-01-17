def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(board):
    # Winning combinations: Rows, Columns, Diagonals
    win_coords = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in win_coords:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Positions are 1-9, starting from top-left.")

    for turn in range(9):
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if board[move] != " ":
                print("Space taken! Try again.")
                continue # This turn doesn't count
        except (ValueError, IndexError):
            print("Invalid input. Enter 1-9.")
            continue

        board[move] = current_player
        
        winner = check_win(board)
        if winner:
            print_board(board)
            print(f"Congratulations! Player {winner} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()