#!/usr/bin/env python3
# coding: UTF-8

import random
import numpy as np

class Board:
    def __init__(self):
        print("ボード表示")

    def board(count, board):
        if count == 0:
            #board = [FILE][RANK]
            board = [
                    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
                    ]
            count += 1

        else:
            a = random.randint(0, 7)
            b = random.randint(0, 7)
            print(a)
            print(b)
            hen = input("入力 -> ")
            board[a][b] = hen
            count += 1

        return board, count
        

    def display(count):
        cp_board = np.empty((8, 8))
        while count < 5:
            cp_board, count = Board.board(count, cp_board)
            print("  a b c d e f g h")
            print(" -----------------")
            for rank in range(8):
                print("{}|".format(8 - rank), end="")
                for file in range(8):
                    print(str(cp_board[rank][file]) + "|", end="")
                print(8 - rank)
            print(" -----------------")
            print("  a b c d e f g h")



def go_play():
    count = 0
    Board.display(count)

if __name__ == "__main__":
    go_play()
