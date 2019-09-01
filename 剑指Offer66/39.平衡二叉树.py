# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:49:12 2019

@author: Tang
"""

'''
题目描述


输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''
import numpy as np
def solution(root):
     
     def digui(root):
          if root==None:
               return 0
          l=digui(root.left)
          r=digui(root.right)
          if l<0 or r<0 or np.ans(l-r)>1:
               return -1
          return max(l,r)+1
     return digui(root)>=0

          
     