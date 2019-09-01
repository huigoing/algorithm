# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:40:36 2019

@author: Tang
"""

'''
题目描述

给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
def solution(node):
     if node==None:
          return None
     if node.right:
          cur=node.right
          while cur.left:
               cur=cur.left
          return cur
     if node.next:
          cur=node
          pre=node.next
          while pre and pre.right==cur:
               cur=pre
               pre=cur.next
          return pre