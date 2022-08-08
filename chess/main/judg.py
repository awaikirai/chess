#!/usr/bin/env python3
# coding: UTF-8

# [駒][リードFILE][リードRANK][駒取得(x)][取得した駒][FILE(縦)][RANK(横)][プロモーション][アンパッサン][チェック・チェックメイト]

import re

def aton(aton):
    fil = "abcdefgh"
    return fil.find(aton)

def cross(aF, aR):
    rf = 7 - aF
    lf = aF - 0
    tr = aR - 0
    br = 7 - aR
    return rf, lf, tr, br

def bFsbRs(board, af, ar, koma, bFs, bRs, count):
    if board[ar][af] == koma:
        bFs += (af) * (10 ** count)
        bRs += (ar) * (10 ** count)
        count += 1
    return bFs, bRs, count



def posi(posi):
    af_F = posi[-2]
    af_R = posi[-1]

    if len(posi) > 2:
        if posi[0].isalpha() == True:
            be_F = aton(posi[0])

            if kihu[1].isalpha() == True:
                be_R = None
                af_F = aton(posi[1])
                af_R = posi[2]
#                print("al_al_nu")

            else:
                be_R = 8 - int(posi[1])
                af_F = aton(posi[2])
                af_R = 8 - int(posi[3])
#                print("al_nu_al_nu")

        else:
            be_F = None
            be_R = int(posi[0])
            af_F = aton(posi[1])
            af_R = 8 - int(posi[2])
#            print("nu_al_nu")
    
    else:
        be_F = None
        be_R = None
        af_F = aton(posi[0])
        af_R = 8 - int(posi[1])
#        print("al_nu")

    

    return be_F, be_R, af_F, af_R


def all_p_j(count, bFs, bRs, be_F, be_R, af_F, af_R):
    if count == 0:
        return 'W', None, None, None
    elif count == 1:
        return bFs, bRs, af_F, af_R
    else:
        if be_F == None and be_R == None:
            return 'W', None, None, None

        elif be_F != None and be_R != None:
            for cou in range(count-1):
                if str(bFs)[cou] == str(be_F) and str(bRs)[cou] == str(be_R):
                    bF = be_F
                    bR = be_R
                    break
                else:
                    bF = 'W'
                    bR = None
            return bF, bR, af_F, af_R

        else:
            for cou in range(count-1):
                if str(bFs)[cou] == str(be_F):
                    if str(bFs).count(str(bFs)[cou]) > 1:
                        bF = 'W'
                        bR = None
                    else:
                        bF = int(str(bFs)[cou])
                        bR = int(str(RFs)[cou])
                    break

                elif str(bRs)[cou] == str(be_R):
                    if str(bRs).count(str(bRs)[cou]) > 1:
                        bF = 'W'
                        bR = None
                    else:
                        bF = int(str(bFs)[cou])
                        bR = int(str(bFs)[cou])
                    break
                else:
                    bF = 'W'
                    bR = None
            return bF, bR, af_F, af_R


def piece(board, koma, pos, turn, castling_count):
    if 'B' in koma:
        be_F, be_R, af_F, af_R = posi(pos)
        count, bFs, bRs = bishop(board, koma, af_F, af_R)
        bF, bR, aF, aR = all_p_j(count, bFs, bRs, be_F, be_R, af_F, af_R)

    elif 'N' in koma:
        be_F, be_R, af_F, af_R = posi(pos)
        count, bFs, bRs = knight(board, koma, af_F, af_R)
        bF, bR, aF, aR = all_p_j(count, bFs, bRs, be_F, be_R, af_F, af_R)

    elif 'R' in koma:
        be_F, be_R, af_F, af_R = posi(pos)
        count, bFs, bRs = rook(board, koma, af_F, af_R)
        bF, bR, aF, aR = all_p_j(count, bFs, bRs, be_F, be_R, af_F, af_R)

    elif 'Q' in koma:
        be_F, be_R, af_F, af_R = posi(pos)
        count, bFs, bRs = queen(board, koma, af_F, af_R)
        bF, bR, aF, aR = all_p_j(count, bFs, bRs, be_F, be_R, af_F, af_R)

    elif 'K' in koma:
        be_F, be_R, af_F, af_R = posi(pos)
        count, bFs, bRs = king(board, koma, af_F, af_R)
        bF, bR, aF, aR = all_p_j(count, bFs, bRs, be_F, be_R, af_F, af_R)

    elif 'P' in koma:
        be_F, be_R, af_F, af_R = posi(pos)
        count, bFs, bRs = Porn(board, koma, af_F, af_R, turn)
        bF, bR, aF, aR = all_p_j(count, bFs, bRs, be_F, be_R, af_F, af_R)

    elif 'qC' in koma or 'kC' in koma:
        bF, bR, aF, aR = castling(turn, koma, castling_count)

    else:
        bF = 'W'
        bR = None
        aF = None
        aR = None

    return bF, bR, aF, aR


def bishop(board, koma, aF, aR):
    count = 0
    bFs = 0
    bRs = 0
    rf, lf, tr, br = cross(aF, aR)
    # top left
    if lf < tr:
        dif = lf
    else:
        dif = tr

    for val in range(1, dif + 1):
        bFs, bRs, count = bFsbRs(board, aF - val, aR - val, koma, bFs, bRs, count)

    # top right
    if rf < tr:
        dif = rf
    else:
        dif = tr

    for val in range(1, dif + 1):
        bFs, bRs, count = bFsbRs(board, aF + val, aR - val, koma, bFs, bRs, count)

    # bottom left
    if lf < br:
        dif = lf
    else:
        dif = br

    for val in range(1, dif + 1):
        bFs, bRs, count = bFsbRs(board, aF - val, aR + val, koma, bFs, bRs, count)

    # bottom right
    if rf < br:
        dif = rf
    else:
        dif = br

    for val in range(1, dif + 1):
        bFs, bRs, count = bFsbRs(board, aF + val, aR + val, koma, bFs, bRs, count)

    return count, bFs, bRs

def knight(board, koma, aF, aR):
    count = 0
    bFs = 0
    bRs = 0
    rf, lf, tr, br = cross(aF, aR)
    # top left
    if tr > 0 and lf > 1:
        bFs, bRs, count = bFsbRs(board, aF - 2, aR - 1, koma, bFs, bRs, count)

    if tr > 1 and lf > 0:
        bFs, bRs, count = bFsbRs(board, aF - 1, aR - 2, koma, bFs, bRs, count)

    # top right
    if tr > 0 and rf > 1:
        bFs, bRs, count = bFsbRs(board, aF + 2, aR - 1, koma, bFs, bRs, count)

    if tr > 1 and rf > 0:
        bFs, bRs, count = bFsbRs(board, aF + 1, aR - 2, koma, bFs, bRs, count)

    # bottom left
    if br > 0 and lf > 1:
        bFs, bRs, count = bFsbRs(board, aF - 2, aR + 1, koma, bFs, bRs, count)

    if br > 1 and lf > 0:
        bFs, bRs, count = bFsbRs(board, aF - 1, aR + 2, koma, bFs, bRs, count)

    # bottom right
    if br > 0 and rf > 1:
        bFs, bRs, count = bFsbRs(board, aF + 2, aR + 1, koma, bFs, bRs, count)

    if br > 0 and rf > 1:
        bFs, bRs, count = bFsbRs(board, aF + 1, aR + 2, koma, bFs, bRs, count)

    return count, bFs, bRs

def rook(board, koma, aF, aR):
    count = 0
    bFs = 0
    bRs = 0
    rf, lf, tr, br = cross(aF, aR)
    # top
    for val in range(1, tr + 1):
        bFs, bRs, count = bFsbRs(board, aF, aR - val, koma, bFs, bRs, count)

    # bottom
    for val in range(1, br + 1):
        bFs, bRs, count = bFsbRs(board, aF, aR + val, koma, bFs, bRs, count)

    # left
    for val in range(1, lf + 1):
        bFs, bRs, count = bFsbRs(board, aF - val, aR, koma, bFs, bRs, count)

    # right
    for val in range(1, rf + 1):
        bFs, bRs, count = bFsbRs(board, aF + val, aR, koma, bFs, bRs, count)

    return count, bFs, bRs

def queen(board, koma, aF, aR):
    count, bFs, bRs = bishop(board, koma, aF, aR)
    se_count, se_bFs, se_bRs = rook(board, koma, aF, aR)
    bFs += (se_bFs) * (10 ** count)
    bRs += (se_bRs) * (10 ** count)
    count += se_count

    return count, bFs, bRs

def king(board, koma, aF, aR):
    count = 0
    bFs = 0
    bRs = 0
    rf, lf, tr, br = cross(aF, aR)
    # round
    if tr != 0:
        bFs, bRs, count = bFsbRs(board, aF, aR - 1, koma, bFs, bRs, count)

    if tr != 0 and lf != 0:
        bFs, bRs, count = bFsbRs(board, aF - 1, aR - 1, koma, bFs, bRs, count)

    if tr != 0 and rf != 0:
        bFs, bRs, count = bFsbRs(board, aF + 1, aR - 1, koma, bFs, bRs, count)

    if br != 0:
        bFs, bRs, count = bFsbRs(board, aF, aR + 1, koma, bFs, bRs, count)

    if br != 0 and lf != 0:
        bFs, bRs, count = bFsbRs(board, aF - 1, aR + 1, koma, bFs, bRs, count)

    if br != 0 and rf != 0:
        bFs, bRs, count = bFsbRs(board, aF + 1, aR + 1, koma, bFs, bRs, count)

    if lf != 0:
        bFs, bRs, count = bFsbRs(board, aF - 1, aR, koma, bFs, bRs, count)

    if rf != 0:
        bFs, bRs, count = bFsbRs(board, aF + 1, aR, koma, bFs, bRs, count)

    return count, bFs, bRs

def Porn(board, koma, aF, aR, turn):
    count = 0
    bFs = 0
    bRs = 0
    rf, lf, tr, br = cross(aF, aR)

    if turn > 0 and tr != 0:
        if board[aR][aF] == 0:
            if aR == 4:
                bFs, bRs, count = bFsbRs(board, aF, aR + 2, koma, bFs, bRs, count)

            bFs, bRs, count = bFsbRs(board, aF, aR + 1, koma, bFs, bRs, count)

        else:
            if '-' in board[aR][aF]:
                if lf == 0:
                    bFs, bRs, count = bFsbRs(board, aF + 1, aR + 1, koma, bFs, bRs, count)
                elif rf == 0:
                    bFs, bRs, count = bFsbRs(board, aF - 1, aR + 1, koma, bFs, bRs, count)
                else:
                    bFs, bRs, count = bFsbRs(board, aF + 1, aR + 1, koma, bFs, bRs, count)
                    bFs, bRs, count = bFsbRs(board, aF - 1, aR + 1, koma, bFs, bRs, count)

    elif turn < 0 and br != 0:
        if board[aR][aF] == 0:
            if aR == 3:
                bFs, bRs, count = bFsbRs(board, aF, aR - 2, koma, bFs, bRs, count)

            bFs, bRs, count = bFsbRs(board, aF, aR - 1, koma, bFs, bRs, count)

        else:
            if '-' not in board[aR][aF]:
                if lf == 0:
                    bFs, bRs, count = bFsbRs(board, aF + 1, aR - 1, koma, bFs, bRs, count)
                elif rf == 0:
                    bFs, bRs, count = bFsbRs(board, aF - 1, aR - 1, koma, bFs, bRs, count)
                else:
                    bFs, bRs, count = bFsbRs(board, aF + 1, aR - 1, koma, bFs, bRs, count)
                    bFs, bRs, count = bFsbRs(board, aF - 1, aR - 1, koma, bFs, bRs, count)

    return count, bFs, bRs
        
def castling(turn, koma, cc):
    # QueenSide Castling
    # KingSide Castling
    if turn > 0 and cc[0] == 0:
        if koma == 'qC' and cc[1] == 0:
            return 2, 7, 3, 7
        elif koma == 'kC' and cc[2] == 0:
            return 6, 7, 5, 7

    elif turn < 0 and cc[3] == 0:
        if koma == 'qC' and cc[4] == 0:
            return 2, 0, 3, 0
        elif koma == 'kC' and cc[5] == 0:
            return 6, 0, 5, 0

    return 'Wc', None, None, None


def screen(turn, board):
    count = 0
    Fs = 0
    Rs = 0
    for R in range(1, 7):
        for F in range(8):
            if turn > 0 and board[R][F] == 'P':
                if F > 0 and board[R - 1][F - 1] != 0 and '-' in board[R - 1][F - 1]:
                    Fs += (F - 1) * (10 ** count)
                    Rs += (R + 1) * (10 ** count)
                    count += 1

                if F < 7 and board[R - 1][F + 1] != 0 and '-' in board[R - 1][F + 1]:
                    Fs += (F + 1) * (10 ** count)
                    Rs += (R + 1) * (10 ** count)
                    count += 1

            elif turn < 0 and board[R][F] == '-P':
                if F > 0 and board[R + 1][F - 1] != 0 and '-' not in board[R + 1][F - 1]:
                    Fs += (F - 1) * (10 ** count)
                    Rs += (R + 1) * (10 ** count)
                    count += 1

                if F < 7 and board[R + 1][F + 1] != 0 and '-' not in board[R + 1][F + 1]:
                    Fs += (F + 1) * (10 ** count)
                    Rs += (R + 1) * (10 ** count)
                    count += 1

    return count, str(Fs), str(Rs)




