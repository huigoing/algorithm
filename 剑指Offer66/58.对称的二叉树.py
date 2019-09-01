# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:46:35 2019

@author: Tang
"""

'''
题目描述

请实现一个函数，用来判断一颗二叉树是不是对称的。注意，
如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''
def solution(root):
     def digui(left , right):
          if left==None:
               return right==None
          if right==None:
               return False
          if left.val!=right.val:
               return False
          return digui(left.left,right.right) and digui(left.right,right.left)
             
     if root==None:
          return True
     return digui(root.left,root.right)
     
     