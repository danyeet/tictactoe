import random

# Define the board and print board method
def print_board(board):
    for row in board:
        print(f"{row[0]} | {row[1]} | {row[2]} ")
    # print(board[0][0] + "|"+ board[0][1] + "|"+ board[0][2])
    # print(board[1][0] + "|"+ board[1][1] + "|"+ board[1][2])
    # print(board[2][0] + "|"+ board[2][1] + "|"+ board[2][2])
    # print()


def isGameOver(board):
    for row in board:
        for i in range(2):
            column = [row[i] for row in board]
            if EMPTY_PLACE in column:
                continue
            elif USER_MOVE in column:
                if CPU_MOVE in column:
                    if USER_MOVE in row:
                        continue
                    else:
                        print("CPU Win - new func. - column")
                        return CPU_MOVE
                else:
                    print("New func test - USER WIN column")
                    return USER_MOVE
                # if i == EMPTY_PLACE:
                #     continue
                # if i == USER_MOVE:
                #     if i + 1 == CPU_MOVE or i + 2 == CPU_MOVE:
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
board = [["", "", USER_MOVE], [USER_MOVE, "", ""], ["", "", ""]]

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
        match winner:
            case "X":
                print("Congratulations, you won!")
                print_board(board)
                break
            case "O":
                print("You lost!")
                print_board(board)
                break
            case _:
                print("It's a tie")
                break
        # Column wins
        # if (
        #     board[0][0] == USER_MOVE
        #     and board[1][0] == USER_MOVE
        #     and board[2][0] == USER_MOVE
        # ):
        #     print("Congratulations, you won!")
        #     print_board(board)
        #     break
        # elif (
        #     board[0][1] == USER_MOVE
        #     and board[1][1] == USER_MOVE
        #     and board[2][1] == USER_MOVE
        # ):
        #     print("Congratulations, you won!")
        #     print_board(board)
        #     break
        # elif (
        #     board[0][2] == USER_MOVE
        #     and board[1][2] == USER_MOVE
        #     and board[2][2] == USER_MOVE
        # ):
        #     print("Congratulations, you won!")
        #     print_board(board)
        #     break
        # Row wins

        # elif (
        #     board[0][0] == USER_MOVE
        #     and board[0][1] == USER_MOVE
        #     and board[0][2] == USER_MOVE
        # ):
        #     print("Congratulations, you won!")
        #     print_board(board)
        #     break
        # elif (
        #     board[1][0] == USER_MOVE
        #     and board[1][1] == USER_MOVE
        #     and board[1][2] == USER_MOVE
        # ):
        #     print("Congratulations, you won!")
        #     print_board(board)
        #     break
        # elif (
        #     board[2][0] == USER_MOVE
        #     and board[2][1] == USER_MOVE
        #     and board[2][2] == USER_MOVE
        # ):
        #     print("Congratulations, you won!")
        #     print_board(board)
        #     break
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
        # while 1:
        #     random_col = random.randint(0, 2)
        #     random_row = random.randint(0, 2)
        #     if board[random_row][random_col] != EMPTY_PLACE:
        #         random_col = random.randint(0, 2)
        #         random_row = random.randint(0, 2)
        #     else:
        #         board[random_row][random_col] = CPU_MOVE
        #         counter_moves += 1
        #         break

        if (
            board[0][0] == CPU_MOVE
            and board[1][0] == CPU_MOVE
            and board[2][0] == CPU_MOVE
        ):
            print("You lost!")
            print_board(board)
            break
        elif (
            board[0][1] == CPU_MOVE
            and board[1][1] == CPU_MOVE
            and board[2][1] == CPU_MOVE
        ):
            print("You lost!")
            print_board(board)
            break
        elif (
            board[0][2] == CPU_MOVE
            and board[1][2] == CPU_MOVE
            and board[2][2] == CPU_MOVE
        ):
            print("You lost!")
            print_board(board)
            break
        # Row wins
        elif (
            board[0][0] == CPU_MOVE
            and board[0][1] == CPU_MOVE
            and board[0][2] == CPU_MOVE
        ):
            print("You lost!")
            print_board(board)
            break
        elif (
            board[1][0] == CPU_MOVE
            and board[1][1] == CPU_MOVE
            and board[1][2] == CPU_MOVE
        ):
            print("You lost!")
            print_board(board)
            break
        elif (
            board[2][0] == CPU_MOVE
            and board[2][1] == CPU_MOVE
            and board[2][2] == CPU_MOVE
        ):
            print("You lost!")
            print_board(board)
            break
        # Diagonal wins
        elif (
            board[0][0] == CPU_MOVE
            and board[1][1] == CPU_MOVE
            and board[2][2] == CPU_MOVE
        ):
            print("You lost!")
            print_board(board)
            break
        elif (
            board[2][0] == CPU_MOVE
            and board[1][1] == CPU_MOVE
            and board[0][2] == CPU_MOVE
        ):
            print("You lost!")
            print_board(board)
            break
        print_board(board)
