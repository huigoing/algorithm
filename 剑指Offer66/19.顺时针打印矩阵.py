# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:29:01 2019

@author: Tang
"""

'''
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，
如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
def solution(a):
     m=len(a)
     n=len(a[0])
     left=0
     right=n-1
     up=0
     down=m-1
     direct=0
     res=[]
     while left<=right or up<=down:
          if direct==0:
               for i in range(left,right+1):
                    res.append(a[up][i])
               up+=1
          elif direct==1:
               for i in range(up,down+1):
                    res.append(a[i][right])
               right-=1
               
          elif direct==2:
               for i  in range(right,left-1,-1):
                    res.append(a[down][i])
               down-=1
               
          elif direct==3:
               for i in range(down,up-1,-1):
                    res.append(a[i][left])
               left+=1
          direct+=1
          direct%=4
     return res
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(solution(a))
               
               
               