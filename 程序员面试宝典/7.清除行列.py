# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:23:55 2019

@author: Tang
"""

'''
题目描述



请编写一个算法，若N阶方阵中某个元素为0，则将其所在的行与列清零。

给定一个N阶方阵int[][](C++中为vector<vector><int>>)mat和矩阵的阶数n，
请返回完成操作后的int[][]方阵(C++中为vector<vector><int>>)，保证n小于等于300，
矩阵中的元素为int范围内。</int></vector></int></vector>

测试样例：
[[1,2,3],[0,1,2],[0,0,1]]
返回：[[0,0,3],[0,0,0],[0,0,0]]
'''
def solution(mat):
     n=len(mat)
     row=set()
     col=set()
     for i in range(n):
          for j in range(n):
               if mat[i][j]==0:
                    row.add(i)
                    col.add(j)
     for i in row:
          for j in range(n):
               mat[i][j]=0
     for i in col:
          for j in range(n):
               mat[j][i]=0
     return mat
a=[[1,2,3],[0,1,2],[0,0,1]]
print(solution(a))