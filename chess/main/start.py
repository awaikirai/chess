#!/usr/bin/env python3
# coding: UTF-8

# [駒][リードFILE][リードRANK][駒取得(x)][取得した駒][FILE(縦)][RANK(横)][プロモーション][アンパッサン][チェック・チェックメイト]

import os
from display import Banmen
import nyuu
import judg
import move

board = [
        ['-R', '-N', '-B', '-Q', '-K', '-B', '-N', '-R'],
        ['-P', '-P', '-P', '-P', '-P', '-P', '-P', '-P'],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

# [WK, WQR, WKR, BK, BQR, BKR]
castling_count = [0, 0, 0, 0, 0, 0]

def king_set(board, kin):
    for sett in range(8):
        if kin in board[sett]:
            if kin == 'K':
                return 1
            elif kin == '-K':
                return -1

    return 0
        


def start(turn, board):
    while turn != 0:
        Banmen.hyouzi(turn, board)
        if turn > 0:
            GR = input("白の手番です -> ")
            koma, posi, kihu = nyuu.kihu(GR)
            if koma == 'W':
                print("もう一度")
                continue

            be_F, be_R, af_F, af_R = judg.piece(board, koma, posi, turn, castling_count)
            if be_F == 'W':
                print("入力に誤りがあります\nもう一度")
                continue
            elif be_F == 'Wc':
                print("そのキャスリングは出来ません\nもう一度")
                continue

            if koma == 'qC' or koma == 'kC':
                if move.c_snip(board, turn, be_F, be_R, af_F, af_R) == 'Wc':
                    print("そのキャスリングは今は出来ません\nもう一度")
                    continue
                board = move.castling(board, koma, 'K', 'R', be_F, be_R, af_F, af_R)
                castling_count[0] = 1

            elif koma == 'R' and be_F == 0:
                if move.obstacle(board, be_F, be_R, af_F, af_R, turn) == False:
                    print("移動先に駒があります\nもう一度")
                    continue
                board = move.moving(board, koma, be_F, be_R, af_F, af_R, turn)
                castling_count[1] = 1

            elif koma == 'R' and be_F == 7:
                if move.obstacle(board, be_F, be_R, af_F, af_R, turn) == False:
                    print("移動先に駒があります\nもう一度")
                    continue
                board = move.moving(board, koma, be_F, be_R, af_F, af_R, turn)
                castling_count[2] = 1

            else:
                if move.obstacle(board, be_F, be_R, af_F, af_R, turn) == False:
                    print("移動先に駒があります\nもう一度")
                    continue
                board = move.moving(board, koma, be_F, be_R, af_F, af_R, turn)

            turn = king_set(board, '-K')



        elif turn < 0:
            print("black")
            GR = input("黒の手番です -> ")
            koma, posi, kihu = nyuu.kihu(GR)
            if koma == 'W':
                print("もう一度")
                continue

            be_F, be_R, af_F, af_R = judg.piece(board, '-' + koma, posi, turn, castling_count)
            if be_F == 'W':
                print("入力に誤りがあります\nもう一度")
                continue
            elif be_F == 'Wc':
                print("そのキャスリングは出来ません\nもう一度")
                continue

            if koma == 'qC' or koma == 'kC':
                if move.c_snip(board, turn, be_F, be_R, af_F, af_R) == 'Wc':
                    print("そのキャスリングは今は出来ません\nもう一度")
                    continue
                board = move.castling(board, koma, '-K', '-R', be_F, be_R, af_F, af_R)
                castling_count[3] = 1

            elif koma == 'R' and be_F == 0:
                if move.obstacle(board, be_F, be_R, af_F, af_R, turn) == False:
                    print("移動先に駒があります\nもう一度")
                    continue
                board = move.moving(board, koma, be_F, be_R, af_F, af_R, turn)
                castling_count[4] = 1

            elif koma == 'R' and be_F == 7:
                if move.obstacle(board, be_F, be_R, af_F, af_R, turn) == False:
                    print("移動先に駒があります\nもう一度")
                    continue
                board = move.moving(board, koma, be_F, be_R, af_F, af_R, turn)
                castling_count[5] = 1

            else:
                if move.obstacle(board, be_F, be_R, af_F, af_R, turn) == False:
                    print("移動先に駒があります\nもう一度")
                    continue
                board = move.moving(board, koma, be_F, be_R, af_F, af_R, turn)

            turn = king_set(board, 'K')


    print("終了！")
    
    if king_set(board, 'K') == 1:
        Banmen.hyouzi(1, board) 
        print("white の勝利")
    elif king_set(board, '-K') == -1:
        Banmen.hyouzi(-1, board)
        print("black の勝利")



def tuitate(turn, board):
    while turn != 0:
        Banmen.screen(turn, board)
        if turn > 0:
            GR = input("白の手番です -> ")
            koma, posi, kihu = nyuu.kihu(GR)
            if koma == 'W':
                print("もう一度")
                continue

            be_F, be_R, af_F, af_R = judg.piece(board, koma, posi, turn, castling_count)
            if be_F == 'W':
                print("入力に誤りがあります\nもう一度")
                continue
            elif be_F == 'Wc':
                print("そのキャスリングは出来ません\nもう一度")
                continue

            if koma == 'qC' or koma == 'kC':
                if move.c_snip(board, turn, be_F, be_R, af_F, af_R) == 'Wc':
                    print("そのキャスリングは今は出来ません\nもう一度")
                    continue
                board = move.castling(board, koma, 'K', 'R', be_F, be_R, af_F, af_R)
                castling_count[0] = 1

            elif koma == 'R' and be_F == 0:
                if move.obstacle(board, be_F, be_R, af_F, af_R, turn) == False:
                    print("移動先に駒があります\nもう一度")
                    continue
                board = move.moving(board, koma, be_F, be_R, af_F, af_R, turn)
                castling_count[1] = 1

            elif koma == 'R' and be_F == 7:
                if move.obstacle(board, be_F, be_R, af_F, af_R, turn) == False:
                    print("移動先に駒があります\nもう一度")
                    continue
                board = move.moving(board, koma, be_F, be_R, af_F, af_R, turn)
                castling_count[2] = 1

            else:
                if move.obstacle(board, be_F, be_R, af_F, af_R, turn) == False:
                    print("移動先に駒があります\nもう一度")
                    continue
                board = move.moving(board, koma, be_F, be_R, af_F, af_R, turn)

            turn = king_set(board, '-K')


        elif turn < 0:
            print("black")
            GR = input("黒の手番です -> ")
            koma, posi, kihu = nyuu.kihu(GR)
            if koma == 'W':
                print("もう一度")
                continue

            be_F, be_R, af_F, af_R = judg.piece(board, '-' + koma, posi, turn, castling_count)
            if be_F == 'W':
                print("入力に誤りがあります\nもう一度")
                continue
            elif be_F == 'Wc':
                print("そのキャスリングは出来ません\nもう一度")
                continue

            if koma == 'qC' or koma == 'kC':
                if move.c_snip(board, turn, be_F, be_R, af_F, af_R) == 'Wc':
                    print("そのキャスリングは今は出来ません\nもう一度")
                    continue
                board = move.castling(board, koma, '-K', '-R', be_F, be_R, af_F, af_R)
                castling_count[3] = 1

            elif koma == 'R' and be_F == 0:
                if move.obstacle(board, be_F, be_R, af_F, af_R, turn) == False:
                    print("移動先に駒があります\nもう一度")
                    continue
                board = move.moving(board, koma, be_F, be_R, af_F, af_R, turn)
                castling_count[4] = 1

            elif koma == 'R' and be_F == 7:
                if move.obstacle(board, be_F, be_R, af_F, af_R, turn) == False:
                    print("移動先に駒があります\nもう一度")
                    continue
                board = move.moving(board, koma, be_F, be_R, af_F, af_R, turn)
                castling_count[5] = 1

            else:
                if move.obstacle(board, be_F, be_R, af_F, af_R, turn) == False:
                    print("移動先に駒があります\nもう一度")
                    continue
                board = move.moving(board, koma, be_F, be_R, af_F, af_R, turn)

            turn = king_set(board, 'K')

        os.system('clear')
        input("準備が出来たら [ENTER]")


    print("終了！")
    
    if king_set(board, 'K') == 1:
        Banmen.hyouzi(1, board) 
        print("white の勝利")
    elif king_set(board, '-K') == -1:
        Banmen.hyouzi(-1, board)
        print("black の勝利")


        

################################################################################


if __name__ == "__main__":
    turn = input("white or black -> ")

    if turn == 'white' or turn == 'black':
        if turn =='white':
            turn = 1
        elif turn == 'black':
            turn = -1

        # start(turn, board)
        tuitate(turn, board)

    else:
        print("white（先手） or black（後手）って聞いとるやん")


