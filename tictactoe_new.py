import random

class Game:
    def __init__(board):
        board = board
    def print_board(board):
        for row in board:
            print(f"{row[0]} | {row[1]} | {row[2]}")
    



if __name__ == "__main__":
    USER_MOVE = "X"
    CPU_MOVE = "O"
    EMPTY_PLACE = ""
    game = Game()
    board = [
    [EMPTY_PLACE, EMPTY_PLACE, EMPTY_PLACE],
    [EMPTY_PLACE, EMPTY_PLACE, EMPTY_PLACE],
    [EMPTY_PLACE, EMPTY_PLACE, EMPTY_PLACE],
]
    game.print_board()