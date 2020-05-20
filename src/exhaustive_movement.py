#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File: exhaustive_movement.py
# @Author: pengjiali
# @Date: 20-5-18
# @Describe:

from chessboard import get_chesspiece_type, get_chesspices_species, ChesspieceSpecies, ChesspieceType, Player, Point, \
    ChessPiece, Chessboard


class ExhaustiveMovement:
    def __init__(self, chessboard, point):
        '''
        穷举在棋牌chessboard上的point点位棋子的所有走法
        NOTE:这个版本的思路是先将可走的路径全部罗列一遍，然后一个点一个点筛查，这种思路很清晰、易实现，但是速度比直接找可走的点要慢点
        :param chessboard:
        :param point:
        '''
        self._chessboard = chessboard
        self._point = point
        self._movement_chesspiece = self._chessboard.get_chesspiece(self._point)
        self._chesspiece_type = get_chesspiece_type(self._movement_chesspiece)
        self._chesspiece_species = get_chesspices_species(self._movement_chesspiece)
        if self._chesspiece_type == ChesspieceType.Empty:
            raise Exception("chesspiece is none in chessboard!")
        elif self._chesspiece_type == ChesspieceType.Black:
            self._player = Player.Black
        else:
            self._player = Player.Red

    def get_all_valid_movement_dst_point(self):
        if self._chesspiece_species == ChesspieceSpecies.General:
            return self._get_general_valid_movement()

    def _get_general_valid_movement(self):
        points = [self._point.relative_point(0, 1), self._point.relative_point(0, -1), self._point.relative_point(1, 0),
                  self._point.relative_point(-1, 0)]

        # 老将不能碰面
        def is_meet(dst_point):
            enemy_general_point = self._chessboard.get_general_point(
                Player.Black if self._player == Player.Red else Player.Red)
            if dst_point.column == enemy_general_point.column:
                if self._is_empyt_between_two_point(dst_point, enemy_general_point):
                    return True
            return False

        points = list(filter(
            lambda point: point.in_royal_palace(self._player) and not self._is_self_mutilation(point) and not is_meet(
                point),
            points))
        return points

    def _is_self_mutilation(self, dst_point):
        '''判断走不标点是否自残'''
        return get_chesspiece_type(self._chessboard.get_chesspiece(dst_point)) == self._chesspiece_type

    def _is_empyt_between_two_point(self, point1, point2):
        '''检测直线上两点之间是否都是空白'''
        if point1 == point2:
            raise Exception("point1 and point2 is same point!")
        elif point1.row == point2.row:
            for row in range(point1.row, point2.row, 1 if point1.row < point2.row else -1):
                if self._chessboard.get_chesspiece(Point(row, point1.column)) != ChessPiece.Empty:
                    return False
        elif point1.column == point2.column:
            for column in range(point1.column, point2.column, 1 if point1.column < point2.column else -1):
                if self._chessboard.get_chesspiece(Point(point1.row, column)) != ChessPiece.Empty:
                    return False
        else:
            raise Exception("point1 and point2 not in the same line!")
        return True


if __name__ == '__main__':
    chessboard = Chessboard()
    chessboard.set_chesspiece(Point(0,3), ChessPiece.BlackBodyGuard)
    chessboard.set_chesspiece(Point(0,4), ChessPiece.BlackGeneral)
    chessboard.set_chesspiece(Point(0,5), ChessPiece.BlackBodyGuard)
    chessboard.set_chesspiece(Point(9,5), ChessPiece.RedGeneral)
    print(chessboard)
    exhaustive_movement = ExhaustiveMovement(chessboard, Point(0, 4))
    points = exhaustive_movement.get_all_valid_movement_dst_point()
    print("Black general valid points:", points)
