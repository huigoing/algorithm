# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:13:50 2019

@author: Tang
"""

'''
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
def solution(tree):
     if tree==None:
          return []
     stack=[tree]
     res=[]
     while stack:
          tmp=stack.pop(0)
          res.append(tmp.val)
          if tmp.left:
               stack.append(tmp.left)
          if tmp.right:
               stack.append(tmp.right)
     return res