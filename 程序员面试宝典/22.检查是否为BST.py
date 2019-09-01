# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:38:01 2019

@author: Tang
"""

'''
题目描述



请实现一个函数，检查一棵二叉树是否为二叉查找树。

给定树的根结点指针TreeNode* root，请返回一个bool，代表该树是否为二叉查找树
'''
def solution(root):
     def dfs(root):
          if root==None:
               return 
          dfs(root.left)
          res.append(root.val)
          dfs(root.right)
     res=[]
     dfs(root)
     if res==sorted(res):
          return True
     else:
          return False