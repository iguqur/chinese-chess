#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File: judge.py
# @Author: pengjiali
# @Date: 20-5-16
# @Describe:

from chessboard import Chessboard, ChessPiece, Player, is_black_chesspiece, is_red_chesspiece, is_empty_chesspiece, \
    Point
from movement import Movement


class Judge:
    def __init__(self, chessboard):
        self._chessboard = chessboard
        self._turn = Player.Red  # 轮到谁走了

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

    def move(self, movement):
        self._check_movement_chesspiece(movement)

        self._move_chesspiece(movement)

    def _check_movement_chesspiece(self, movement):
        '''检测被移动的棋子是否合法'''
        movement_chesspiece = self._chessboard.get_chesspiece(movement.start_point)
        if is_empty_chesspiece(movement_chesspiece):
            raise Exception("movement chesspiece is empty!")
        elif is_black_chesspiece(movement_chesspiece):
            if self._turn == Player.Red:
                raise Exception("Red player turn, but movement chesspiece is black!")
        elif is_red_chesspiece(movement_chesspiece):
            if self._turn == Player.Black:
                raise Exception("Red player turn, but movement chesspiece is black!")

    def _move_chesspiece(self, movement):
        self._chessboard.set_chesspiece(movement.end_point, self._chessboard.get_chesspiece(movement.start_point))
        self._chessboard.set_chesspiece(movement.start_point, ChessPiece.Empty)


if __name__ == '__main__':
    chessboard = Chessboard()
    judge = Judge(chessboard)
    judge.reset()
    # print(chessboard)
    movement = Movement(Point(6, 2), Point(5, 2))
    judge.move(movement)
    print(chessboard)
