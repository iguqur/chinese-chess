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


def is_black_chesspiece(chesspiece):
    return chesspiece.value > 0 and chesspiece.value < 10


def is_red_chesspiece(chesspiece):
    return chesspiece.value > 10


def is_empty_chesspiece(chesspiece):
    return chesspiece == ChessPiece.Empty


def get_chesspiece_type(chesspiece):
    if is_empty_chesspiece(chesspiece):
        return ChesspieceType.Empty
    elif is_black_chesspiece(chesspiece):
        return ChesspieceType.Black
    else:
        return ChesspieceType.Red


class ChesspieceType(Enum):
    Empty = 0
    Black = 1
    Red = 2


class Player(Enum):
    Black = 0
    Red = 1


class Point:
    '''
    点格
    '''

    def __init__(self, row, column):
        self.row = row
        self.column = column


class Chessboard:
    '''
    棋盘
    右手系，[0][0]表示棋盘左上角的格点，[0][4]表示黑帅的位置
    上面是黑棋，下面是红棋
    '''

    def __init__(self):
        self._chessboard = [[ChessPiece.Empty] * 9 for _ in range(10)]

    def get_chesspiece(self, point):
        return self._chessboard[point.row][point.column]

    def set_chesspiece(self, point, chess_piece):
        self._chessboard[point.row][point.column] = chess_piece

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
                    if is_empty_chesspiece(chesspiece):
                        font_start = '\033[33m'
                    elif is_black_chesspiece(chesspiece):
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
                if (i == 0 or i == 2 or i == 7 or i == 9) and (j == 3 or j == 4):
                    ret += "\033[33m——\033[0m"
                else:
                    ret += "  "
                j += 1
            ret += "\n"
            if i == 0 or i == 7:
                ret += "\033[33m" + " " * 11 + '| ＼' + " " * 2 + "／ |\033[0m\n"
            elif i == 1 or i == 8:
                ret += "\033[33m" + " " * 11 + '| ／' + " " * 2 + "＼ |\033[0m\n"
            else:
                ret += "\n"
            i += 1
        return ret


if __name__ == '__main__':
    chessboard = Chessboard()
    print(chessboard)
