# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:24:08 2019

@author: Tang
"""

'''
题目描述


给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

中序遍历
'''
def solution(root,k):
     if root==None or k<=0:
          return None
     res=[]
     inorder(root,res)
     if len(res)<k:
          return None
     else:
          return res[k-1]
def inorder(root,res):
     if root==None:
          return
     inorder(root.left,res)
     res.append(root.val)
     inorder(root.right,res)
     