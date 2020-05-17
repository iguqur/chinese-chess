#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   movement.py
@Time    :   2020/05/17 16:15:39
@Author  :   pengjiali
@Version :   1.0
@Desc    :   
'''

from chessboard import Point


class Movement(object):
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point