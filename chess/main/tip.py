#!/usr/bin/env python3
# coding: UTF-8

# [駒][リードFILE][リードRANK][駒取得(x)][取得した駒][FILE(横)][RANK(縦)][プロモーション][アンパッサン][チェック・チェックメイト]

def cross(aF, aR):
    rf = 7 - aF
    lf = aF - 0
    tr = aR - 0
    br = 7 - aR

    return rf, lf, tr, br

def bishop(aF, aR):
    count = 0
    rf, lf, tr, br = cross(aF, aR)
    # top left
    if lf < tr:
        dif = lf
    else:
        dif = tr

    for val in range(dif):
        if board[aR - val][aF - val] = 'B':
            count += 1

    # top right
    if rf < tr:
        dif = rf
    else:
        dif = tr

    for val in range(dif):
        if board[aR - val][aF - val] = 'B':
            count += 1

   # bottom left
    if lf < br:
        dif = lf
    else:
        dif = br

    for val in range(dif):
        if board[aR - val][aF - val] = 'B':
            count += 1

   # bottom right
    if rf < br:
        dif = rf
    else:
        dif = br

    for val in range(dif):
        if board[aR - val][aF - val] = 'B':
            count += 1

    return count

