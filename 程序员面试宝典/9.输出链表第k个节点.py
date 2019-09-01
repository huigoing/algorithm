# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:52:34 2019

@author: Tang
"""

'''
题目描述


输入一个链表，输出该链表中倒数第k个结点。
'''
def solution(head,k):
     res=[]
     p=head
     while p:
          res.append(p.val)
     if k>len(res) or k<1:
          return []
     else:
          return res[-k]