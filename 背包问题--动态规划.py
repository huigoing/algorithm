# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:00:11 2019

@author: Tang
"""

import sys


def track(d, c, w):                                              #输出最优路径
    x = []
    for i in range(len(w), 1, -1):                               #m[n][c]为最优值，如果m[n][c]=m[n-1][c] ,说明有没有第n件物品都一样
        if d[i][c] != d[i - 1][c]:
            x.append(w[i - 1])
            c = c - w[i - 1]
    if d[1][c] > 0:
        x.append(w[0])

    return x

if __name__ == '__main__':
    v = [8, 10, 6, 3, 7, 2]
    w = [4, 6, 2, 2, 5, 1]
    c=12

    dp = [[0] * (c + 1) for i in range(len(w) + 1)]             #动态规划矩阵

    for i in range(1, len(w) + 1):
        for j in range(1, c + 1):
            if j >= w[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])         #动态转移方程
            else:
                dp[i][j] = dp[i - 1][j]

    print (max(dp[len(w)]) )                                      #输出最大值

    print (track(dp, c, w)  )                                     #输出最优路径
