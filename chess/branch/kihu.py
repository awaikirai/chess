#!/usr/bin/env python3
# coding: UTF-8

def kihu(koma):
    if koma[-1] == "+":
        print("check")
        f.write(koma)

    elif koma[-1] == "#":
        print("check_mate")
        f.write(koma)

    else:
        f.write(koma)



fini = True
f = open("men.txt", "w")
while fini == True:
    wh = input("white -> ")
    kihu(wh)
    f.write(" ")
    bl = input("black -> ")
    kihu(bl)
    f.write("\n")
f.close()
