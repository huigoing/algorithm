# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:37:46 2019

@author: Tang
"""

'''
题目描述
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''
def solution(root,n):
     def dfs(root,n,res,result):
          res.append(root)
          if root and root.left==None and root.right==None and root.val==res:
               result.append(res)
          if root.left:
               dfs(root.left,n-root.val,list(res),result)
          if root.right:
               dfs(root.right,n-root.val,list(res),result)
     if root==None:
          return []
     result=[]
     dfs(root,n,[],result)
     return result

     