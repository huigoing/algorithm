# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:36:47 2019

@author: Tang
"""

'''
题目描述


输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''
def solution(root):
     if root==None:
          return root
     if root.left==None and root.right==None:
          return root
     solution(root.left)
     left=root.left
     if left:
          while left.right:
               left=left.right
          root.left,left.right=left,root
     solution(root.right)
     right=root.right
     if right:
          while right.left:
               right=right.left
          root.right,right.left=right,root
     while root.left:
          root=root.left
     return root