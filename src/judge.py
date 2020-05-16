#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File: judge.py
# @Author: pengjiali
# @Date: 20-5-16
# @Describe:

from chessboard import Chessboard, ChessPiece

class Judge:
    def __init__(self, chessboard):
        self._chessboard = chessboard

    def reset(self):
        chessboard = [[ChessPiece.Empty] * 9 for _ in range(10)]
        chessboard[0][0] = ChessPiece.BlackCar
        chessboard[0][1] = ChessPiece.BlackHorse
        chessboard[0][2] = ChessPiece.BlackElephant
        chessboard[0][3] = ChessPiece.BlackBodyGuard
        chessboard[0][4] = ChessPiece.BlackGeneral
        chessboard[0][5] = ChessPiece.BlackBodyGuard
        chessboard[0][6] = ChessPiece.BlackElephant
        chessboard[0][7] = ChessPiece.BlackHorse
        chessboard[0][8] = ChessPiece.BlackCar

        chessboard[2][1] = ChessPiece.BlackCannon
        chessboard[2][7] = ChessPiece.BlackCannon

        chessboard[3][0] = ChessPiece.BlackSoldier
        chessboard[3][2] = ChessPiece.BlackSoldier
        chessboard[3][4] = ChessPiece.BlackSoldier
        chessboard[3][6] = ChessPiece.BlackSoldier
        chessboard[3][8] = ChessPiece.BlackSoldier

        chessboard[9][0] = ChessPiece.RedCar
        chessboard[9][1] = ChessPiece.RedHorse
        chessboard[9][2] = ChessPiece.RedElephant
        chessboard[9][3] = ChessPiece.RedBodyGuard
        chessboard[9][4] = ChessPiece.RedGeneral
        chessboard[9][5] = ChessPiece.RedBodyGuard
        chessboard[9][6] = ChessPiece.RedElephant
        chessboard[9][7] = ChessPiece.RedHorse
        chessboard[9][8] = ChessPiece.RedCar

        chessboard[7][1] = ChessPiece.RedCannon
        chessboard[7][7] = ChessPiece.RedCannon

        chessboard[6][0] = ChessPiece.RedSoldier
        chessboard[6][2] = ChessPiece.RedSoldier
        chessboard[6][4] = ChessPiece.RedSoldier
        chessboard[6][6] = ChessPiece.RedSoldier
        chessboard[6][8] = ChessPiece.RedSoldier

        self._chessboard.set_chesspieces(chessboard)

if __name__ == '__main__':
    chessboard = Chessboard()
    judge = Judge(chessboard)
    judge.reset()
    print(chessboard)