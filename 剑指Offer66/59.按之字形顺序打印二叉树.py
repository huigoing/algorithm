# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:00:48 2019

@author: Tang
"""

'''
题目描述


请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''
def solution(root):
     
     stack=[root]
     result=[]
     flag=1
     while stack:
          tmp=[]
          res=[]
          for i in stack:
               res.append(i.val)
               if i.left:
                    tmp.append(i.left)
               if i.right:
                    tmp.append(i.right)
          stack=tmp
          if flag:
               result.append(res)
               flag=0
          else:
               result.append(res[::-1])
               flag=1
     return result
          
               
          