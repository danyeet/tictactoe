import random
# Define the board and print board method
def print_board(board):
    print(board[0][0] + "|"+ board[0][1] + "|"+ board[0][2])
    print(board[1][0] + "|"+ board[1][1] + "|"+ board[1][2])
    print(board[2][0] + "|"+ board[2][1] + "|"+ board[2][2])
    print()

board = [["","",""],
         ["","",""],
         ["","",""]]

if __name__ == "__main__":
    counter_moves = 0
    print_board(board)
    # Game logic
    while 1:
        usr_input_col = int(input("Enter column number between 1 and 3:")) - 1
        usr_input_row = int(input("Enter row number between 1 and 3:")) - 1
        while 1:
            if usr_input_col > 2 or usr_input_col < 0:
                usr_input_col = int(input("Please enter a valid column number between 1 and 3:")) - 1
            elif usr_input_row > 2 or usr_input_row < 0:
                usr_input_row = int(input("Please enter a valid row number between 1 and 3:")) - 1
            elif board[usr_input_row][usr_input_col] != "":
                print("Please enter a position that is correct and not already used.")
                usr_input_col = int(input("Enter column number between 1 and 3:")) - 1
                usr_input_row = int(input("Please enter a valid row number between 1 and 3:")) - 1
            else:
                break
        board[usr_input_row][usr_input_col] = "X"
        counter_moves += 1
        
        # Column wins
        if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
            print("Congratulations, you won!")
            print_board(board)
            break
        elif board[0][1] == "X" and board[1][1]  == "X" and board[2][1] == "X":
            print("Congratulations, you won!")
            print_board(board)
            break
        elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
            print("Congratulations, you won!")
            print_board(board)
            break
        # Row wins
        elif board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
            print("Congratulations, you won!")
            print_board(board)
            break
        elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
            print("Congratulations, you won!")
            print_board(board)
            break
        elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
            print("Congratulations, you won!")
            print_board(board)
            break
        # Diagonal wins
        elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
            print("Congratulations, you won!")
            print_board(board)
            break
        elif board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
            print("Congratulations, you won!")
            print_board(board)
            break
        # Tie condition
        if counter_moves == 9:
            print("It's a tie")
            print_board(board)
            break
        while 1:    
            random_col = random.randint(0,2)
            random_row = random.randint(0,2)
            if board[random_row][random_col] != "":
                random_col = random.randint(0,2)
                random_row = random.randint(0,2)
            else:
                board[random_row][random_col] = "O"
                counter_moves += 1
                break
        if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
            print("You lost!")
            print_board(board)
            break
        elif board[0][1] == "O" and board[1][1]  == "O" and board[2][1] == "O":
            print("You lost!")
            print_board(board)
            break
        elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
            print("You lost!")
            print_board(board)
            break
        # Row wins
        elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
            print("You lost!")
            print_board(board)
            break
        elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
            print("You lost!")
            print_board(board)
            break
        elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
            print("You lost!")
            print_board(board)
            break
        # Diagonal wins
        elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
            print("You lost!")
            print_board(board)
            break
        elif board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
            print("You lost!")
            print_board(board)
            break
        print_board(board)