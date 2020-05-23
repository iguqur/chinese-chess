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
    return 0 < chesspiece.value < 10


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


def get_chesspices_species(chesspiece):
    if chesspiece == ChessPiece.BlackGeneral or chesspiece == ChessPiece.RedGeneral:
        return ChesspieceSpecies.General
    elif chesspiece == ChessPiece.BlackBodyGuard or chesspiece == ChessPiece.RedBodyGuard:
        return ChesspieceSpecies.BodyGard
    elif chesspiece == ChessPiece.BlackElephant or chesspiece == ChessPiece.RedElephant:
        return ChesspieceSpecies.Elephant
    elif chesspiece == ChessPiece.BlackHorse or chesspiece == ChessPiece.RedHorse:
        return ChesspieceSpecies.Horse
    elif chesspiece == ChessPiece.BlackCar or chesspiece == ChessPiece.RedCar:
        return ChesspieceSpecies.Car
    elif chesspiece == ChessPiece.BlackCannon or chesspiece == ChessPiece.RedCannon:
        return ChesspieceSpecies.Cannon
    elif chesspiece == ChessPiece.BlackSoldier or chesspiece == ChessPiece.RedSoldier:
        return ChesspieceSpecies.Soldier
    else:
        return ChesspieceSpecies.Empty


class ChesspieceType(Enum):
    Empty = 0
    Black = 1
    Red = 2


class ChesspieceSpecies(Enum):
    Empty = 0
    General = 1
    BodyGard = 2
    Elephant = 3
    Horse = 4
    Car = 5
    Cannon = 6
    Soldier = 7


class Player(Enum):
    Black = 0
    Red = 1


class Point:
    '''
    点格
    '''
    MIN_ROW = 0
    MIN_COLUMN = 0
    MAX_ROW = 9
    MAX_COLUMN = 8

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def valid(self):
        return 0 <= self.row <= Point.MAX_ROW and 0 <= self.column <= Point.MAX_COLUMN

    def relative_point(self, row, column):
        '''
        返回当前点的相对位置的点
        :param row:
        :param column:
        :return:
        '''
        return Point(self.row + row, self.column + column)

    def in_royal_palace(self, player):
        '''
        判断点是否在皇宫里
        :param player: 那方的皇宫
        :return:
        '''
        if player == Player.Black:
            return 0 <= self.row <= 2 and 3 <= self.column <= 5
        else:
            return 7 <= self.row <= 9 and 3 <= self.column <= 5

    def is_cross_the_river(self, player):
        '''判断是否过河了'''
        if player == Player.Black:
            return self.row >= 5
        else:
            return self.row < 5

    def __repr__(self):
        return "(%d, %d)" % (self.row, self.column)


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

    def is_empty_chesspiece(self, point):
        return is_empty_chesspiece(self._chessboard[point.row][point.column])

    def is_not_empty_chesspiece(self, point):
        return not is_empty_chesspiece(self._chessboard[point.row][point.column])

    def get_general_point(self, player):
        if player == Player.Black:
            for row in range(0, 3):
                for column in range(3, 6):
                    if self._chessboard[row][column] == ChessPiece.BlackGeneral:
                        return Point(row, column)
        else:
            for row in range(7, 10):
                for column in range(3, 6):
                    if self._chessboard[row][column] == ChessPiece.RedGeneral:
                        return Point(row, column)
        raise Exception("Can not find general!")

    def __repr__(self):
        ret = "    零  一  二  三  四  五  六  七  八  \n"
        i = 0
        for row in self._chessboard:
            row_str = str(i) + ")  " # 有格子线的行
            row_padding_str = '   ' # 格子线之间的填充行
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

                row_str += chinese(chesspiece, i, j)
                if (i == 0 or i == 2 or i == 7 or i == 9) and (j == 3 or j == 4):
                    row_str += "\033[33m——\033[0m"
                else:
                    row_str += "  "
                j += 1
            if i == 4:
                row_padding_str += '\033[32m' + "-" * 8 + "楚河" + "-" * 9 + "汉界" + "-" * 8 + '\033[0m'
            elif i == 0 or i == 7:
                row_padding_str += "\033[33m" + " " * 11 + '| ＼' + " " * 2 + "／ |\033[0m"
            elif i == 1 or i == 8:
                row_padding_str += "\033[33m" + " " * 11 + '| ／' + " " * 2 + "＼ |\033[0m"
            ret += row_str + "\n"
            ret += row_padding_str + "\n"
            i += 1
        ret = ret[:-4]
        ret += "    零  一  二  三  四  五  六  七  八 "
        return ret


if __name__ == '__main__':
    chessboard = Chessboard()
    print(chessboard)
