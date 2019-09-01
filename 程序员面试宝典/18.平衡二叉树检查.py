# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:09:48 2019

@author: Tang
"""

'''
题目描述



实现一个函数，检查二叉树是否平衡，平衡的定义如下，对于树中的任意一个结点，其两颗子树的高度差不超过1。

给定指向树根结点的指针TreeNode* root，请返回一个bool，代表这棵树是否平衡。
'''
def solution(root):
     def depth(root):
          if root==None:
               return 0
          return 1+max(depth(root.left),depth(root.right))
     if root==None:
          return True
     return solution(root.left) and solution(root.right) and abs(depth(root.left)-depth(root.right)<=1)