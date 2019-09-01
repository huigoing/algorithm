# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:59:13 2019

@author: Tang
"""

'''
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
def solution(a,b):
     def digui(a,b):
          if b==None:
               return True
          if a==None or a.val!=b.val:
               return False
          return digui(a.left,b.left) and digui(a.right,b.right)
     if a==None or b==None:
          return False
     return digui(a,b) or digui(a.left,b) or digui(a.right,b)