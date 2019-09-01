# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:17:58 2019

@author: Tang
"""

'''
题目描述
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''
def dayin(head):
     res=[]
     p=head
     if p==None:
          return res
     while p:
          res.append(p.val)
          p=p.next
     return res[::-1]