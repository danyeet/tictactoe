import random

# Define the board and print board method
def print_board(board):
    for row in board:
        print(f"{row[0]} | {row[1]} | {row[2]} ")


def isGameOver(board):
    for row in board:
        for i in range(2):
            column = [row[i] for row in board]
            if EMPTY_PLACE in column:
                continue
            elif USER_MOVE in column:
                if CPU_MOVE in column:
                    if USER_MOVE in column:
                        continue
                    else:
                        print("CPU Win - new func. - column")
                        return CPU_MOVE
                else:
                    print("New func test - USER WIN column")
                    return USER_MOVE
        # diag1 = []
        # diag2 = []
        # for i in range(2):
        #     diag1.append(row[i])

        if EMPTY_PLACE in row:
            continue
        elif CPU_MOVE in row:
            if USER_MOVE in row:
                continue
            else:
                print("CPU Win - new func. - row")
                return CPU_MOVE
        else:
            print("New func works - user win. - row")
            return USER_MOVE


USER_MOVE = "X"
CPU_MOVE = "O"
EMPTY_PLACE = ""
board = [["", "", ""], [CPU_MOVE, "", ""], [CPU_MOVE, "", ""]]

if __name__ == "__main__":
    counter_moves = 0
    print_board(board)
    # Game logic
    while 1:
        usr_input_col = int(input("Enter column number between 1 and 3:")) - 1
        usr_input_row = int(input("Enter row number between 1 and 3:")) - 1
        while 1:
            if usr_input_col > 2 or usr_input_col < 0:
                usr_input_col = (
                    int(input("Please enter a valid column number between 1 and 3:"))
                    - 1
                )
            elif usr_input_row > 2 or usr_input_row < 0:
                usr_input_row = (
                    int(input("Please enter a valid row number between 1 and 3:")) - 1
                )
            elif board[usr_input_row][usr_input_col] != EMPTY_PLACE:
                print("Please enter a position that is correct and not already used.")
                usr_input_col = int(input("Enter column number between 1 and 3:")) - 1
                usr_input_row = (
                    int(input("Please enter a valid row number between 1 and 3:")) - 1
                )
            else:
                break
        board[usr_input_row][usr_input_col] = USER_MOVE
        counter_moves += 1

        # New func test
        # isGameOver(board)
        winner = isGameOver(board)
        if winner == USER_MOVE:
            print("Congratulations, you won!!")
            print_board(board)
            break
        elif winner == CPU_MOVE:
            print("You lost!")
            print_board(board)
            break
        elif winner == EMPTY_PLACE:
            print("It's a tie")
            print_board(board)
            break
        # Column wins
        # Diagonal wins
        if (
            board[0][0] == USER_MOVE
            and board[1][1] == USER_MOVE
            and board[2][2] == USER_MOVE
        ):
            print("Congratulations, you won!")
            print_board(board)
            break
        elif (
            board[2][0] == USER_MOVE
            and board[1][1] == USER_MOVE
            and board[0][2] == USER_MOVE
        ):
            print("Congratulations, you won!")
            print_board(board)
            break
        # Tie condition
        # if counter_moves == 9:
        #     print("It's a tie")
        #     print_board(board)
        #     break
        while 1:
            random_col = random.randint(0, 2)
            random_row = random.randint(0, 2)
            if board[random_row][random_col] != EMPTY_PLACE:
                random_col = random.randint(0, 2)
                random_row = random.randint(0, 2)
            else:
                board[random_row][random_col] = CPU_MOVE
                counter_moves += 1
                break
        print_board(board)
