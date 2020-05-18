#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File: exhaustive_movement.py
# @Author: pengjiali
# @Date: 20-5-18
# @Describe:

from chessboard import Chessboard, ChessPiece, Player, is_black_chesspiece, is_red_chesspiece, is_empty_chesspiece, \
    Point, ChesspieceType, get_chesspiece_type
from movement import Movement


class ExhaustiveMovement:
    def __init__(self, chessboard, point):
        '''
        穷举在棋牌chessboard上的point点位棋子的所有走法
        :param chessboard:
        :param point:
        '''
        self._chessboard = chessboard
        self._point = point
        self._movement_chesspiece = self._chessboard.get_chesspiece(self._point)
        self._chesspiece_type = get_chesspiece_type(self._movement_chesspiece)

    def get_all_valid_movement_dst_point(self):
        if self._chesspiece_type == ChesspieceType.Empty:
            return []
