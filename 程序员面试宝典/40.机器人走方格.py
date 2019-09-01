# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:15:48 2019

@author: Tang
"""
'''
题目描述

有一个XxY的网格，一个机器人只能走格点且只能向右或向下走，要从左上角走到右下角。请设计一个算法，
计算机器人有多少种走法。

给定两个正整数int x,int y，请返回机器人的走法数目。保证x＋y小于等于12。

测试样例：
2,2
返回：2
'''
#方法1
def countWays( x, y):
        # write code here
        def dfs(a,b):
            if a==x-1 or b==y-1:
                return 1
            if a>=0 and a<x and b>=0 and b<y:
                #self.count+=1
                print(111)
                return dfs(a+1,b) + dfs(a,b+1)
        return dfs(0,0)
print(countWays(3,3))

#方法2
def solution(x,y):
     res=[[0 for i in range(y)] for j in range(x)]
     for i in range(x):
          res[i][0]=1
     for i in range(y):
          res[0][i]=1
     for i in range(1,x):
          for j in range(1,y):
               res[i][j]=res[i-1][j]+res[i][j-1]
     return res[x-1][y-1]
print(solution(3,3))
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     