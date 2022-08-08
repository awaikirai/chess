#!/usr/bin/env python3
# coding: UTF-8

import judg


# [駒][リードFILR][リードRANK][駒取得(x)][取得した駒][FILE(縦)][RANK(横)][プロモーション][アンパッサン][チェック・チェックメイト]

class Banmen:
    def hyouzi(turn, board):
        if turn > 0:
            print("  a  b  c  d  e  f  g  h")
            print(" -------------------------")
            for rank in range(8):
                print("{}|".format(8 - rank), end="")
                for file in range(8):
                    if str(board[rank][file]) == '0':
                        print("  |", end="")

                    elif str('-') in str(board[rank][file]) != True:
                        print('\033[31m' + str(board[rank][file]).replace('-', '') + '\033[0m' + " |", end="")

                    else:
                        print(str(board[rank][file]) + " |", end="")

                print(8 - rank)
                print(" -------------------------")
            print("  a  b  c  d  e  f  g  h")

        elif turn < 0:
            print("  h  g  f  e  d  c  b  a")
            print(" -------------------------")
            for rank in reversed(range(8)):
                print("{}|".format(8 - rank), end="")
                for file in reversed(range(8)):
                    if str(board[rank][file]) == '0':
                        print("  |", end="")

                    elif str('-') in str(board[rank][file]) != True:
                        print('\033[31m' + str(board[rank][file]).replace('-', '') + '\033[0m' + " |", end="")

                    else:
                        print(str(board[rank][file]) + " |", end="")

                print(8 - rank)
                print(" -------------------------")
            print("  h  g  f  e  d  c  b  a")

        else:
            print("ERROR")


    def screen(turn, board):
        if turn > 0:
            print("  a  b  c  d  e  f  g  h")
            print(" -------------------------")
            for rank in range(8):
                print("{}|".format(8 - rank), end="")
                for file in range(8):
                    if str(board[rank][file]) == '0' or '-' in str(board[rank][file]):
                        print("  |", end="")

                    else:
                        print(str(board[rank][file]) + " |", end="")

                print(8 - rank)
                print(" -------------------------")
            print("  a  b  c  d  e  f  g  h")

        elif turn < 0:
            print("  h  g  f  e  d  c  b  a")
            print(" -------------------------")
            for rank in reversed(range(8)):
                print("{}|".format(8 - rank), end="")
                for file in reversed(range(8)):
                    if str(board[rank][file]) == '0' or '-' not in str(board[rank][file]):
                        print("  |", end="")

                    else:
                        print('\033[31m' + str(board[rank][file]).replace('-', '') + '\033[0m' + " |", end="")
                        
                print(8 - rank)
                print(" -------------------------")
            print("  h  g  f  e  d  c  b  a")

        else:
            print("ERROR")

        count, Fs, Rs = judg.screen(turn, board)
        if count > 0:
            print("ポーンでとれる駒の位置は")
            Fc = "abcdefgh"
            for i in range(count):
                print("{}{}".format(Fc[int(Fs[i])], Rs[i]))
            print("です")


       

###########################################################################


'''
if __name__ == "__main__":
    board = [
            ['-R', '-N', '-B', '-Q', '-K', '-B', '-N', '-R'],
            ['-P', '-P', '-P', '-P', '-P', '-P', '-P', '-P'],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

    Banmen.hyouzi(1, board)
'''

