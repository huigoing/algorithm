# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:40:34 2019

@author: Tang
"""

'''
题目描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结
点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''
def solution(root):
     if root==None:
          return 0
     l=solution(root.left)
     r=solution(root.right)
     return max(l,r)+1