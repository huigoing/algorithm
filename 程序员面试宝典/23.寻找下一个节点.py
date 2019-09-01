# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:41:33 2019

@author: Tang
"""

'''
题目描述



请设计一个算法，寻找二叉树中指定结点的下一个结点（即中序遍历的后继）。

给定树的根结点指针TreeNode* root和结点的值int p，请返回值为p的结点的后继结点的值。
保证结点的值大于等于零小于等于100000且没有重复值，若不存在后继返回-1。
'''
def solution(root):
     def dfs(root):
          if root==None:
               return 
          dfs(root.left)
          res.append(root.val)
          dfs(root.right)
     res=[]
     for i in range(len(res)):
          if res[i]==p and i<len(res)-1:
               return res[i+1]
     return -1