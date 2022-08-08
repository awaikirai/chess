#!/usr/bin/env python3
# coding: UTF-8

import re

def hantei(ga_re):
    if len(ga_re) < 2:
        print("FALSE")

    # キングサイドキャスリング
    elif ga_re == "O-O" or ga_re == "0-0":
        print("キングキャスリング")
    
    # クイーンサイドキャスリング
    elif ga_re == "O-O-O" or ga_re == "0-0-0":
        print("クインキャスリング")

    elif ga_re in ["K", "Q", "R", "N", "B", "P", "x", "=", "+", "#"]:
        if ga_le[0] == ["K", "Q", "R", "N", "B"]:
            print("SUCCES")

        else:
            print("FALSE")

    else:
        print("FALSE")


def go():
    game_record = input("棋譜通りに => ")
    hantei(game_record)


if __name__ == "__main__":
    go()
