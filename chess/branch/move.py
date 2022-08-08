#!/usr/bin/env python3
# coding: UTF-8

import random

class Koma:
    def w_porn(be_F, be_R, af_F, af_R):
        if af_R == 8 and af_R not in ["R", "N", "B", "P"]:
            print("プロモーション")
            return False
        
        if be_R - af_R == 1 and af_F == be_F and board[af_R][af_F] == 0:
            # 1前進
            return True

        if abs(af_F - be_F) == 1 and be_R - af_R == 1 and board[af_R][af_F] != 0:
            # 斜め
            return True

        if be_R == 2 and board[af_R][af_F] == 0 and board[af_R+1][af_F] == 0:
            #　2マス進む
            return True

        # アンパッサンが残ってる



    def b_porn(be_F, be_R, af_F, af_R):
        if af_R == 1 and af_P not in ["r", "n", "b", "p"]:
            print("プロモーション")
            return False

        if af_R - be_R == 1 and af_F == be_F and board[af_R][af_F] == 0:
            return True

        if abs(af_F - be_F) == 1 and af_R - be_R == 1 and board[af_R][af_F] != 0:
            return True

        if be_R == 7 and board[af_R][af_F] == 0 and board[af_R+1][af_F] == 0:
            return True


    def rook(be_F, be_R, af_F, af_R):
        if be_F != af_F and be_R != af_R:
            return False

    def knight(be_F, be_R, af_F, af_R):
        if (abs(be_F - af_F) == 1 and abs(af_R - be_R) == 2) or (abs(be_F - af_F) == 2 and abs(af_R - be_R) == 1):
            return True

    def bishop(be_F, be_R, af_F, af_R):
        if abs(be_F - af_F) != abs(be_R - af_R):
            return False

    def queen(be_F, be_R, af_F, af_R):
        if (abs(be_F - af_F) != abs(be_R - af_R)) and (be_F != af_F and be_R != af_R):
            return False

    def king(be_F, be_R, af_F, af_R):
        if abs(be_F - af_F) <= 1 and abs(be_R - af_R) <= 1:
            return True
        
    # キャスリング用
    #


def after(af_F, af_R, af_P):
    if af_P == 0 and board[af_R+1][af_F] == "P":
        board[af_R][af_F] = P
        board[af_R][af_F] = 0


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

FILE = ["a", "b", "c", "d", "e", "f", "g", "h"]
PIECE = ["P", "B", "N", "R", "Q", "K"]

af_f = random.randint(0, 7)
af_r = random.randint(0, 7)
af_p = random.randint(0, 5)

print(PIECE[af_p], end='')
print(FILE[af_f], end='')
print(af_r + 1)

after(af_f, af_r, af_p)
print(board)







