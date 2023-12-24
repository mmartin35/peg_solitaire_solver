import sys
import time

# Define the initial peg arrangement
# 0 = empty, 1 = busy, 2 = wall
initial_board = [
    [2, 2, 1, 1, 1, 2, 2],
    [2, 2, 1, 1, 1, 2, 2],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [2, 2, 1, 1, 1, 2, 2],
    [2, 2, 1, 1, 1, 2, 2],
]

class Positions:
    def __init__(move, x, y)
        move.x = x
        move.y = y

def draw_board(board):
    for row in board:
        print(row)

# d = direction of try (0 = up, 1 = right, 2 = down, 3 = left)
def owr_board(board, x, y, d):
    board[y][x] = 0
    switch_dict = {
        0:  board[y + 1][x] = 0
            board[y + 2][x] = 1
        1:  board[y][x + 1] = 0
            board[y][x + 2] = 1
        2:  board[y - 1][x] = 0
            board[y - 2][x] = 1
        3:  board[y][x - 1] = 0
            board[y][x - 2] = 1
    }
    return board

def try_move(board, pos):
    while (1):
        if (board[pos.y][pos.x])

def main():
    timeout = 10000
    b = 32
    board = initial_board
    while (b != 1 || timeout != 0):
        pos = Postions(random.randint(1, 7), random.randint(1. 7))
        while (board[pos.y][pos.x] = 2):
            pos = Postions(random.randint(1, 7), random.randint(1. 7))
        if (try_move(board, pos) == 0):
            owr_board(board, pos)
            b--
        else:
            timeout--

        draw_board(board)
        time.sleep(1)

main()
