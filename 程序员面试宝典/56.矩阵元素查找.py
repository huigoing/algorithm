# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:39:00 2019

@author: Tang
"""

'''
题目描述



有一个NxM的整数矩阵，矩阵的行和列都是从小到大有序的。请设计一个高效的查找算法，查找矩阵中元素x的位置。

给定一个int有序矩阵mat，同时给定矩阵的大小n和m以及需要查找的元素x，请返回一个二元数组，代表该元素的行号和列号(均从零开始)。保证元素互异。

测试样例：
[[1,2,3],[4,5,6]],2,3,6
返回：[1,2]
'''
def findElement(mat, n, m, x):
        # write code here
        r=n-1
        c=0
        while r>=0 and c<m:
            if mat[r][c]<x:
                c+=1
            elif mat[r][c]==x:
                return [r,c]
            else:
                r-=1