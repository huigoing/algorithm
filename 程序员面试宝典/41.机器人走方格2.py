# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 14:52:33 2019

@author: Tang
"""

'''
题目描述



有一个XxY的网格，一个机器人只能走格点且只能向右或向下走，要从左上角走到右下角。请设计一个算法，
计算机器人有多少种走法。注意这次的网格中有些障碍点是不能走的。

给定一个int[][] map(C++ 中为vector>),表示网格图，若map[i][j]为1则说明该点不是障碍点，否则则为障碍。
另外给定int x,int y，表示网格的大小。请返回机器人从(0,0)走到(x - 1,y - 1)的走法数，为了防止溢出，
请将结果Mod 1000000007。保证x和y均小于等于50
'''
def solution(m,x,y):
        if len(m)!=x or len(m[0])!=y or m==None:
            return 0
        if m[x-1][y-1]!=1 or m[0][0]!=1:
            return 0
        res=[[0]*y for i in range(x)]
        res[0][0]=1
        for i in range(1,x):
            if m[i][0]==1:
                res[i][0]=res[i-1][0]
        for i in range(1,y):
            if m[0][i]==1:
                res[0][i]=res[0][i-1]
        for i in range(1,x):
            for j in range(1,y):
                if m[i][j]==1:
                    res[i][j]=res[i-1][j]%1000000007+res[i][j-1]%1000000007
        return res[x-1][y-1]%1000000007