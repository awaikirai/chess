#!/usr/bin/env python3
# coding: UTF-8

# [駒][リードFILE][リードRANK][駒取得(x)][取得した駒][FILE(縦)][RANK(横)][プロモーション][アンパッサン][チェック・チェックメイト]

def obstacle(board, bF, bR, aF, aR, turn):
    # x
    if abs(bF - aF) == abs(bR - aR):
        # L
        if bF > aF and bR > aR or bF < aF and bR < aR:
            if bF > aF:
                for dif in range(1, bF - aF):
                    if board[bR - dif][bF - dif] != 0:
                        print(1)
                        return False
            else:
                for dif in range(1, aF - bF):
                    if board[aR - dif][aF - dif] != 0:
                        print(2)
                        return False
        # /
        else:
            if bF > aF:
                for dif in range(1, bF - aF):
                    if board[bR + dif][bF - dif] != 0:
                        print(3)
                        return False
            else:
                for dif in range(1, aF - bF):
                    if board[bR - dif][bF + dif] != 0:
                        print(4)
                        return False

    # +
    elif bF - aF == 0 or bR - aR == 0:
        # l
        if bF - aF == 0:
            if bR > aR:
                for dif in range(1, bR - aR):
                    if board[bR - dif][bF] != 0:
                        print(5)
                        return False

            else:
                for dif in range(1, aR - bR):
                    if board[aR - dif][bF] != 0:
                        print(6)
                        return False
        # -
        else:
            if bF > aF:
                for dif in range(1, bF - aF):
                    if board[bR][bF - dif] != 0:
                        print(7)
                        return False

            else:
                for dif in range(1, aF - bF):
                    if board[bR][aF - dif] != 0:
                        print(8)
                        return False

    if board[aR][aF] != 0:
        if turn > 0 and '-' not in str(board[aR][aF]):
            print(9)
            return False

        elif turn < 0 and '-' in str(board[aR][aF]):
            print(0)
            return False



def kni_snip(rev, ove, board, wF, wR):
    if board[wR - 1 * rev][wF - 2] == ove:
        return 'Wc'
    if board[wR - 2 * rev][wF - 1] == ove:
        return 'Wc'
    if board[wR - 2 * rev][wF + 1] == ove:
        return 'Wc'
    if wF < 6 and board[wR - 1 * rev][wF + 2] == ove:
        return 'Wc'

def kp_snip(rev, ove, board, wF, wR):
    if board[wR - 1 * rev][wF - 1] == ove:
        return 'Wc'
    if board[wR - 1 * rev][wF + 1] == ove:
        return 'Wc'



def c_snip(board, turn, kF, kR, rF, rR):
    if turn > 0:        
        for lu in range(1, kF + 1):
            if board[kR - lu][kF - lu] != 0:
                if '-' in board[kR - lu][kF - lu]:
                    if 'Q' in board[kR - lu][kF - lu] or 'B' in board[kR - lu][kF - lu]:
                        return 'Wc'
                break

        for lu in range(1, rF + 1):
            if board[rR - lu][rF - lu] != 0:
                if '-' in board[rR - lu][rF - lu]:
                    if 'Q' in board[rR - lu][rF - lu] or 'B' in board[rR - lu][rF - lu]:
                        return 'Wc'
                break

        for ru in range(1, 7 - kF):
            if board[kR - ru][kF + ru] != 0:
                if '-' in board[kR - ru][kF + ru]:
                    if 'Q' in board[kR - ru][kF + ru] or 'B' in board[kR - ru][kF + ru]:
                        return 'Wc'
                break

        for ru in range(1, 7 - rF):
            if board[rR - ru][rF + ru] != 0:
                if '-' in board[rR - ru][rF + ru]:
                    if 'Q' in board[rR - ru][rF + ru] or 'B' in board[rR - ru][rF + ru]:
                        return 'Wc'
                break

        for ud in range(1, 8):
            if board[kR - ud][kF] != 0:
                if '-' in board[kR - ud][kF]:
                    if 'Q' in board[kR - ud][kF] or 'R' in board[kR - ud][kF]:
                        return 'Wc'
                break

        for ud in range(1, 8):
            if board[rR - ud][rF] != 0:
                if '-' in board[rR - ud][rF]:
                    if 'Q' in board[rR - ud][rF] or 'R' in board[rR - ud][rF]:
                        return 'Wc'
                break

        if kni_snip(1, '-N', board, kF, kR) == 'Wc':
            return 'Wc'
        if kni_snip(1, '-N', board, rF, rR) == 'Wc':
            return 'Wc'

        if kp_snip(1, '-P', board, kF, kR) == 'Wc':
            return 'Wc'
        if kp_snip(1, '-P', board, rF, rR) == 'Wc':
            return 'Wc'
        if kp_snip(1, '-K', board, kF, kR) == 'Wc':
            return 'Wc'
        if kp_snip(1, '-K', board, rF, rR) == 'Wc':
            return 'Wc'
  

    if turn < 0:        
        for lu in range(1, kF + 1):
            if board[kR + lu][kF - lu] != 0:
                if '-' not in board[kR + lu][kF - lu]:
                    if 'Q' in board[kR + lu][kF - lu] or 'B' in board[kR + lu][kF - lu]:
                        return 'Wc'
                break

        for lu in range(1, rF + 1):
            if board[rR + lu][rF - lu] != 0:
                if '-' not in board[rR + lu][rF - lu]:
                    if 'Q' in board[rR + lu][rF - lu] or 'B' in board[rR + lu][rF - lu]:
                        return 'Wc'
                break

        for ru in range(1, 7 - kF):
            if board[kR + ru][kF + ru] != 0:
                if '-' not in board[kR + ru][kF + ru]:
                    if 'Q' in board[kR + ru][kF + ru] or 'B' in board[kR + ru][kF + ru]:
                        return 'Wc'
                break

        for ru in range(1, 7 - rF):
            if board[rR + ru][rF + ru] != 0:
                if '-' not in board[rR + ru][rF + ru]:
                    if 'Q' in board[rR + ru][rF + ru] or 'B' in board[rR + ru][rF + ru]:
                        return 'Wc'
                break

        for ud in range(1, 8):
            if board[kR + ud][kF] != 0:
                if '-' not in board[kR + ud][kF]:
                    if 'Q' in board[kR + ud][kF] or 'R' in board[kR + ud][kF]:
                        return 'Wc'
                break

        for ud in range(1, 8):
            if board[rR + ud][rF] != 0:
                if '-' not in board[rR + ud][rF]:
                    if 'Q' in board[rR + ud][rF] or 'R' in board[rR + ud][rF]:
                        return 'Wc'
                break

        if kni_snip(-1, 'N', board, kF, kR) == 'Wc':
            return 'Wc'
        if kni_snip(-1, 'N', board, rF, rR) == 'Wc':
            return 'Wc'
 
        if kp_snip(-1, 'P', board, kF, kR) == 'Wc':
            return 'Wc'
        if kp_snip(-1, 'P', board, rF, rR) == 'Wc':
            return 'Wc'
        if kp_snip(-1, 'K', board, kF, kR) == 'Wc':
            return 'Wc'
        if kp_snip(-1, 'K', board, rF, rR) == 'Wc':
            return 'Wc'


def castling(board, koma, kg, rk, kF, kR, rF, rR):
    board[kR][kF] = kg
    board[rR][rF] = rk
    board[kR][4] = 0
    if koma == 'qC':
        board[rR][0] = 0
    elif koma == 'kC':
        board[rR][7] = 0
    return board
    


def moving(board, koma, bF, bR, aF, aR, turn):
    if turn > 0:
        board[bR][bF] = 0
        board[aR][aF] = koma

    elif turn < 0:
        board[bR][bF] = 0
        board[aR][aF] = '-' + koma

    return board



'''    
if __name__ == "__main__":
    moving(board, bF, bR, aF, aR)
'''

