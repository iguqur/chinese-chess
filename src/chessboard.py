#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File: chessboard.py
# @Author: pengjiali
# @Date: 20-5-13
# @Describe:


from enum import Enum


class ChessPiece(Enum):
    Empty = 0

    BlackGeneral = 1
    BlackBodyGuard = 2
    BlackElephant = 3
    BlackHorse = 4
    BlackCar = 5
    BlackCannon = 6
    BlackSoldier = 7

    RedBGeneral = 11
    RedBodyGuard = 12
    RedElephant = 13
    RedHorse = 14
    RedCar = 15
    RedCannon = 16
    RedSoldier = 17


class Chessboard():
    def __init__(self):
        self._chessboard = [[ChessPiece.Empty] * 9] * 10

    def __repr__(self):
        ret = ""
        i = 0
        for row in self._chessboard:
            i += 1
            if i == 6:
                ret += "-" * 9 + "楚河" + "-" * 10 + "汉界" + "-" * 9
                ret += "\n\n"
            for chesspiece in row:
                ret += "{0:02d}".format(chesspiece.value)
                ret += "  "
            ret += "\n\n"
        return ret


if __name__ == '__main__':
    chessboard = Chessboard()
    print(chessboard)
