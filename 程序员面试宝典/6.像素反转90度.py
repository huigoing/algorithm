# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:07:07 2019

@author: Tang
"""

'''
题目描述



有一副由NxN矩阵表示的图像，这里每个像素用一个int表示，请编写一个算法，在不占用额外内存空间的情
况下(即不使用缓存矩阵)，将图像顺时针旋转90度。

给定一个NxN的矩阵，和矩阵的阶数N,请返回旋转后的NxN矩阵,保证N小于等于500，图像元素小于等于256。

测试样例：
[[1,2,3],[4,5,6],[7,8,9]],3
返回：[[7,4,1],[8,5,2],[9,6,3]]

先i行与n-i-1行交换 再主对角线交换
'''
def solution(mat):
     n=len(mat[0])
     for i in range(n//2):
          tmp=mat[i]
          mat[i]=mat[n-i-1]
          mat[n-i-1]=tmp
     for i in range(1,n):
          for j in range(i):
               mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
     return mat
a=[[1,2,3],[4,5,6],[7,8,9]]
print(solution(a))
          