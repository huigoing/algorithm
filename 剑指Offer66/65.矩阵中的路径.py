# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:22:14 2019

@author: Tang
"""

'''
题目描述


请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 
这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b
占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''

def solution(a,s,rows,cols):
     def digui(a,s,rows,cols,i,j):
          if len(s)==0:
               return True
          a[i*cols+j]='0'
          if j+1<cols and a[i*cols+j+1]==s[0]:#向右
               return digui(a,s[1:],rows,cols,i,j+1)
          elif j-1>=0 and a[i*cols+j-1]==s[0]: #向左
               return digui(a,s[1:],rows,cols,i,j-1)
          elif i-1>=0 and a[(i-1)*cols+j]==s[0]: #向上
               return digui(a,s[1:],rows,cols,i-1,j)
          elif i+1>=0 and a[(i+1)*cols+j]==s[0]:#向下
               return digui(a,s[1:],rows,cols,i+1,j)
          else:
               return False
     for i in range(rows):
          for j in range(cols):
               if a[i*cols+j]==s[0]:
                    return digui(a,s[1:],rows,cols,i,j)
               
               