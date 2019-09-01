# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:11:33 2019

@author: Tang
"""

'''
题目描述


输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义
为从树的根结点开始
往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
'''
def solution(root,k):
     def dfs(root,k,res,result):
          res.append(root.val)
          if root and not root.left and not root.right and k==root.val:
               result.append(res)
          if root.left:
               dfs(root.left,k-root.val,list(res),result)
          if root.right:
               dfs(root.right,k-root.val,list(res),result)
     res=[]
     result=[]
     if root==None:
          return result
     dfs(root,k,res,result)
     return result
     
          