from tictactoe import create_board, place_move, print_board, check_win, check_draw, find_best_move

def main():
    board = create_board()
    print_board(board)

    while True:
        """ Player 1 Move"""
        row, col = map(int, input("Enter your move (row col): ").split())
        if place_move(board, row, col, 1):
            print_board(board)
            if check_win(board, 1):
                print("You win!")
                break
            if check_draw(board):
                print("It's a draw!")
                break

            """ AI Move"""
            ai_move = find_best_move(board)
            place_move(board, ai_move[0], ai_move[1], 2)
            print("AI moved:")
            print_board(board)
            if check_win(board, 2):
                print("AI wins!")
                break
            if check_draw(board):
                print("It's a draw!")
                break
        else:
            print("Invalid move, try again.")

if __name__ == "__main__":
    main()
