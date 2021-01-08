import time
import os
# Squares = numbers 1-9
# Each number can only appear once in a row, column or square

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def print_board(board):
    # simple board print
    cols = [2, 5]
    count = 0
    for i in range(0, 9):
        for j in board[i]:
            print(j, end=" ")

            if count in cols:
                print('| ', end='')
            count += 1

        print('')
        count = 0

        if i in cols:
            print('-'*21)
    print('')


def empty_square():
    # determines if square is a 0 (empty)
    global board
    for j in range(0, 9):
        for i in range(0, 9):
            if board[j][i] == 0:
                return j, i


def valid(num, pos):
    # determines valid number
    global board
    y, x = pos

    # row
    for i in range(0, 9):
        if num == board[y][i]:
            return False
    # column
    for i in range(0, 9):
        if num == board[i][x]:
            return False

    # 3x3 square
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[y0+i][x0+j] == num:
                return False
    return True


def solve():
    # solves board
    global board
    if empty_square() is not None:
        y, x = empty_square()
        for num in range(1, 10):
            if valid(num, (y, x)):
                board[y][x] = num
                solve()
                board[y][x] = 0
        return
    print('After:')
    print_board(board)


print('Before:')
print_board(board)
start = time.time()
solve()
end = time.time()
print('Done!')
print(f'Completed in:{(end - start): .2f} seconds')
print('')
