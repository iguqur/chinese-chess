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

    RedGeneral = 11
    RedBodyGuard = 12
    RedElephant = 13
    RedHorse = 14
    RedCar = 15
    RedCannon = 16
    RedSoldier = 17


class Chessboard:
    '''
    棋盘
    左手系，[0][0]表示棋盘左上角的格点
    上面是黑棋，下面是红棋
    '''

    def __init__(self):
        self._chessboard = [[ChessPiece.Empty] * 9 for _ in range(10)]

    def set_chesspiece(self, row, column, chess_piece):
        self._chessboard[row][column] = chess_piece

    def set_chesspieces(self, chessboard):
        self._chessboard = chessboard

    def __repr__(self):
        ret = ""
        i = 0
        for row in self._chessboard:
            if i == 5:
                ret += '\033[32m' + "-" * 8 + "楚河" + "-" * 9 + "汉界" + "-" * 8 + '\033[0m'
                ret += "\n\n"
            j = 0
            for chesspiece in row:
                def chinese(chesspiece, i, j):
                    font_end = '\033[0m'
                    if chesspiece.value == 0:
                        font_start = '\033[33m'
                    elif chesspiece.value < 10:
                        font_start = '\033[30m'
                    else:
                        font_start = '\033[31m'

                    if chesspiece == ChessPiece.BlackGeneral:
                        name = '将'
                    elif chesspiece == ChessPiece.BlackBodyGuard:
                        name = '士'
                    elif chesspiece == ChessPiece.BlackElephant:
                        name = '象'
                    elif chesspiece == ChessPiece.BlackHorse:
                        name = '馬'
                    elif chesspiece == ChessPiece.BlackCar:
                        name = '車'
                    elif chesspiece == ChessPiece.BlackCannon:
                        name = '炮'
                    elif chesspiece == ChessPiece.BlackSoldier:
                        name = '卒'
                    elif chesspiece == ChessPiece.RedGeneral:
                        name = '帥'
                    elif chesspiece == ChessPiece.RedBodyGuard:
                        name = '仕'
                    elif chesspiece == ChessPiece.RedElephant:
                        name = '相'
                    elif chesspiece == ChessPiece.RedHorse:
                        name = '馬'
                    elif chesspiece == ChessPiece.RedCar:
                        name = '車'
                    elif chesspiece == ChessPiece.RedCannon:
                        name = '炮'
                    elif chesspiece == ChessPiece.RedSoldier:
                        name = '兵'
                    else:
                        if (i == 2 and j == 1) or (i == 2 and j == 7) \
                                or (i == 3 and j == 0) or (i == 3 and j == 2) or (i == 3 and j == 4) or (
                                i == 3 and j == 6) or (i == 3 and j == 8) or \
                                (i == 7 and j == 1) or (i == 7 and j == 7) \
                                or (i == 6 and j == 0) or (i == 6 and j == 2) or (i == 6 and j == 4) or (
                                i == 6 and j == 6) or (i == 6 and j == 8):
                            name = '卍'
                        else:
                            name = '〇'
                    return font_start + name + font_end

                ret += chinese(chesspiece, i, j)
                ret += "  "
                j += 1
            ret += "\n\n"
            i += 1
        return ret


if __name__ == '__main__':
    chessboard = Chessboard()
    print(chessboard)
