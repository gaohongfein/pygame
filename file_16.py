#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Gao hongfei
#Time: 2018.03.01
import math

class Vector2(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    @classmethod
    def from_points(cls, P1, P2):
        return cls(P2[0] - P1[0], P2[1] - P1[1] )
        # 我们可以使用下面的方法来计算两个点之间的向量
    def get_magnitude(self):
        return math.sqrt(self.x**2+self.y**2)
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude
    def __add__(self, other):
        return Vector2(self.x+other.x,self.y+other.y)
    def __sub__(self, other):
        return Vector2(self.x-other.x,self.y-other.y)
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    def __div__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)


A = (10.0, 20.0)
B = (30.0, 35.0)
AB = Vector2.from_points(A, B)
print(AB.__str__())
print(type(AB))
print(AB.get_magnitude())
AB.normalize()
print(AB.x,AB.y)
print(AB*2)
print(AB+AB+AB)

