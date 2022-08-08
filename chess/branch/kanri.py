#!/usr/bin/env python3
# coding: UTF-8

w_b = 0
mate = 0
while True:
    # キングをとる
    if int(mate) == 1:
        # 勝者を決めて
        print("King")
        break

    # チェックメイト
    if int(mate) == 2:
        print("Checkmate")
        break

    # ステイルメイト
    if int(mate) == 3:
        print("Stalemate")
        break

    mate = input("1, 2, 3でGAMESET") 

print("GAMESET")
