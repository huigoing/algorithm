# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:00:45 2019

@author: Tang
"""

'''
题目描述



在二维平面上，有两个正方形，请找出一条直线，能够将这两个正方形对半分。假定正方形的上下两条边与x轴平行。

给定两个vecotrA和B，分别为两个正方形的四个顶点。请返回一个vector，代表所求的平分直线的斜率和截距，保证斜率存在。

测试样例：
[(0,0),(0,1),(1,1),(1,0)],[(1,0),(1,1),(2,0),(2,1)]
返回：[0.0，0.5]

思路：直接计算就好了,因为能平分两正方形的直线必然经过两个正方形的中心点
算出两正方形中心点的位置，即得到了位置

'''
def getBipartition(self, A, B):
        # write code here
        ax=0
        ay=0
        for i in A:
            ax+=i.x
            ay+=i.y
        ax/=4.0
        ay/=4.0
        bx=0
        by=0
        for i in B:
            bx+=i.x
            by+=i.y
        bx/=4.0
        by/=4.0
        k=(ay-by)/(ax-bx)
        b=ay-k*ax
        return k,b