# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:04:36 2019

@author: Tang
"""

'''
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
'''
def find(a,n):
     row=len(a)
     col=len(a[0])
     i=row-1
     j=0
     while i>=0 and j<col:
          tmp=a[i][j]
          if tmp<n:
               j+=1
          elif tmp>n:
               i-=1
          else:
               return True
     return False
a=[[1,3,5,],[2,4,7],[3,6,9]]
print(find(a,8))