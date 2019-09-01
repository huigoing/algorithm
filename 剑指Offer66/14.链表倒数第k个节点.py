# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:21:45 2019

@author: Tang
"""

'''
题目描述
输入一个链表，输出该链表中倒数第k个结点。
'''
def solution(head,k):
     if head==None:
          return None
     
     res=[]
     while head:
          res.append(head.val)
          head=head.next
     if k>len(res) or k<1:
          return None
     return res[-k]
