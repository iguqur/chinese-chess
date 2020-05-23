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
        elif self._chesspiece_species == ChesspieceSpecies.BodyGard:
            return self._get_body_guard_valid_movement()
        elif self._chesspiece_species == ChesspieceSpecies.Elephant:
            return self._get_elephant_valid_movement()
        elif self._chesspiece_species == ChesspieceSpecies.Horse:
            return self._get_horse_valid_movement()
        elif self._chesspiece_species == ChesspieceSpecies.Car:
            return self._get_car_valid_movement()
        elif self._chesspiece_species == ChesspieceSpecies.Cannon:
            return self._get_cannon_valid_movement()
        elif self._chesspiece_species == ChesspieceSpecies.Soldier:
            return self._get_soldier_valid_movement()

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

    def _get_body_guard_valid_movement(self):
        points = [self._point.relative_point(1, 1), self._point.relative_point(1, -1),
                  self._point.relative_point(-1, -1),
                  self._point.relative_point(-1, 1)]

        points = list(filter(
            lambda point: point.in_royal_palace(self._player) and not self._is_self_mutilation(point),
            points))
        return points

    def _get_elephant_valid_movement(self):
        points = [self._point.relative_point(2, 2), self._point.relative_point(2, -2),
                  self._point.relative_point(-2, -2),
                  self._point.relative_point(-2, 2)]

        def is_stuck(point):
            '''蹩脚'''
            return self._chessboard.is_not_empty_chesspiece(
                Point(int((self._point.row + point.row) / 2), int((self._point.column + point.column) / 2)))

        points = list(filter(
            lambda point: point.valid() and not point.is_cross_the_river(
                self._player) and not is_stuck(point) and not self._is_self_mutilation(
                point),
            points))

        return points

    def _get_horse_valid_movement(self):
        points = [self._point.relative_point(2, 1),
                  self._point.relative_point(2, -1),
                  self._point.relative_point(1, 2),
                  self._point.relative_point(1, -2),
                  self._point.relative_point(-1, 2),
                  self._point.relative_point(-1, -2),
                  self._point.relative_point(-2, 1),
                  self._point.relative_point(-2, -1)]

        def is_stuck(point):
            '''蹩脚'''
            if point.row - self._point.row == 2:
                return self._chessboard.is_not_empty_chesspiece(self._point.relative_point(1, 0))
            elif point.row - self._point.row == -2:
                return self._chessboard.is_not_empty_chesspiece(self._point.relative_point(-1, 0))
            elif point.column - self._point.column == 2:
                return self._chessboard.is_not_empty_chesspiece(self._point.relative_point(0, 1))
            else:
                return self._chessboard.is_not_empty_chesspiece(self._point.relative_point(0, -1))

        points = list(filter(
            lambda point: point.valid() and not is_stuck(point) and not self._is_self_mutilation(
                point),
            points))

        return points

    def _get_car_valid_movement(self):
        # 此处用代码可读性换取速度
        points = []

        def check_point(point):
            '''
            检查当前point是否可以走，只是提取公共代码而已
            :param point:
            :return: True -- 需要继续往下迭代； False -- 不需要继续迭代了
            '''
            chesspiece_type = get_chesspiece_type(self._chessboard.get_chesspiece(point))
            if chesspiece_type == ChesspieceType.Empty:
                points.append(point)
                return True
            elif chesspiece_type == self._chesspiece_type:
                return False
            else:
                points.append(points)
                return False

        for row in range(self._point.row, Point.MIN_ROW, -1):
            row += -1
            point = Point(row, self._point.column)
            if not check_point(point):
                break
        for row in range(self._point.row, Point.MAX_ROW):
            row += 1
            point = Point(row, self._point.column)
            if not check_point(point):
                break
        for column in range(self._point.column, Point.MIN_COLUMN, -1):
            column += -1
            point = Point(self._point.row, column)
            if not check_point(point):
                break
        for column in range(self._point.column, Point.MAX_COLUMN):
            column += 1
            point = Point(self._point.row, column)
            if not check_point(point):
                break
        return points

    def _get_cannon_valid_movement(self):
        points = []
        eat_mode = False  # 跳了一个棋子就开始吃子模式，否则是正常的走

        def check_point(point):
            '''
            检查当前point是否可以走，只是提取公共代码而已
            :param point:
            :return: True -- 需要继续往下迭代； False -- 不需要继续迭代了
            '''
            chesspiece_type = get_chesspiece_type(self._chessboard.get_chesspiece(point))
            nonlocal eat_mode
            if not eat_mode:
                if chesspiece_type == ChesspieceType.Empty:
                    points.append(point)
                elif chesspiece_type == self._chesspiece_type:
                    eat_mode = True
                else:
                    eat_mode = True
                return True
            else:
                if chesspiece_type == ChesspieceType.Empty:
                    return True
                elif chesspiece_type == self._chesspiece_type:
                    return False
                else:
                    points.append(point)
                    return False

        for row in range(self._point.row, Point.MIN_ROW, -1):
            row += -1
            point = Point(row, self._point.column)
            if not check_point(point):
                break
        eat_mode = False
        for row in range(self._point.row, Point.MAX_ROW):
            row += 1
            point = Point(row, self._point.column)
            if not check_point(point):
                break
        eat_mode = False
        for column in range(self._point.column, Point.MIN_COLUMN, -1):
            column += -1
            point = Point(self._point.row, column)
            if not check_point(point):
                break
        eat_mode = False
        for column in range(self._point.column, Point.MAX_COLUMN):
            column += 1
            point = Point(self._point.row, column)
            if not check_point(point):
                break

        return points

    def _get_soldier_valid_movement(self):
        points = [self._point.relative_point(0, 1), self._point.relative_point(0, -1)]
        if self._player == Player.Black:
            points.append(self._point.relative_point(1, 0))
        else:
            points.append(self._point.relative_point(-1, 0))

        points = list(filter(
            lambda point: point.valid() and not self._is_self_mutilation(point),
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
    chessboard.set_chesspiece(Point(0, 0), ChessPiece.BlackCar)
    chessboard.set_chesspiece(Point(0, 1), ChessPiece.BlackHorse)
    chessboard.set_chesspiece(Point(0, 2), ChessPiece.BlackElephant)
    chessboard.set_chesspiece(Point(0, 3), ChessPiece.BlackBodyGuard)
    chessboard.set_chesspiece(Point(0, 4), ChessPiece.BlackGeneral)
    chessboard.set_chesspiece(Point(0, 5), ChessPiece.BlackBodyGuard)
    chessboard.set_chesspiece(Point(2, 1), ChessPiece.BlackCannon)
    chessboard.set_chesspiece(Point(3, 0), ChessPiece.BlackSoldier)
    chessboard.set_chesspiece(Point(9, 5), ChessPiece.RedGeneral)
    chessboard.set_chesspiece(Point(7, 1), ChessPiece.RedCannon)
    chessboard.set_chesspiece(Point(9, 1), ChessPiece.RedHorse)
    print(chessboard)
    exhaustive_movement = ExhaustiveMovement(chessboard, Point(0, 4))
    points = exhaustive_movement.get_all_valid_movement_dst_point()
    print("Black general valid points:", points)

    exhaustive_movement = ExhaustiveMovement(chessboard, Point(0, 3))
    points = exhaustive_movement.get_all_valid_movement_dst_point()
    print("Black body guard valid points:", points)

    exhaustive_movement = ExhaustiveMovement(chessboard, Point(0, 2))
    points = exhaustive_movement.get_all_valid_movement_dst_point()
    print("Black elephant valid points:", points)

    exhaustive_movement = ExhaustiveMovement(chessboard, Point(0, 1))
    points = exhaustive_movement.get_all_valid_movement_dst_point()
    print("Black horse valid points:", points)

    exhaustive_movement = ExhaustiveMovement(chessboard, Point(0, 0))
    points = exhaustive_movement.get_all_valid_movement_dst_point()
    print("Black car valid points:", points)

    exhaustive_movement = ExhaustiveMovement(chessboard, Point(2, 1))
    points = exhaustive_movement.get_all_valid_movement_dst_point()
    print("Black cannon valid points:", points)

    exhaustive_movement = ExhaustiveMovement(chessboard, Point(3, 0))
    points = exhaustive_movement.get_all_valid_movement_dst_point()
    print("Black soldier valid points:", points)
