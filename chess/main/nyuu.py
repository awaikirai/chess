#!/usr/bin/env python3
# coding: UTF-8

import re


# [駒][リードFILE][リードRANK][駒取得(x)][取得した駒][FILE(縦)][RANK(横)][プロモーション][アンパッサン][チェック・チェックメイト]
# [キャスリング]


def kihu(kihu):
    go = re.match(r"^[PBNRQK]?[a-h]?[1-8]?x?[PBNRQK]?[a-h][1-8](=?[BNRQ]|(e.p.))?[\+#]?", kihu)

    if go:
        kihu = go.group()

        if kihu[0] in ['B', 'N', 'R', 'Q', 'K']:
            if 'e.p.' in kihu[1:] or 'B' in kihu[1:] or 'N' in kihu[1:] or 'R' in kihu[1:] or 'Q' in kihu[1:]:
                return 'W', None, None

            else:
                koma = kihu[0]
                posi = re.sub('[PBNRQKx\+#]', '', kihu)
                return koma, posi, kihu

        else:
            koma = 'P'
            posi = re.sub('[=PBNRQx\+#]', '', kihu)
            return koma, posi, kihu

    elif kihu == 'o-o-o' or kihu == 'O-O-O' or kihu == '0-0-0':
        koma = 'qC'
        kihu = 'O-O-O'
        return koma, None, kihu

    elif kihu == 'o-o' or kihu == 'O-O' or kihu == '0-0':
        koma = 'kC'
        kihu = 'O-O'
        return koma, None, kihu

    else:
        return 'W', None, None


'''
if __name__ == "__main__":
    aaa = input("GO -> ")
    a, b, c = kihu(aaa)
    print(a, b, c)
'''

