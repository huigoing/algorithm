# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:16:12 2019

@author: Tang
"""

'''
题目描述


从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''
def solution(root):
     if root==None:
          return None
     stack=[root]
     result=[]
     while stack:
          res=[]
          tmp=[]
          while stack:
               n=stack.pop()
               res.append(n.val)
               tmp.append(n)
          result.append(res)
          while tmp:
               m=tmp.pop()
               if m.right:
                    stack.append(m.right)
               if m.left:
                    stack.append(m.left)
     return result
                    