# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:25:58 2019

@author: Tang
"""

'''
题目描述
输入一个链表，反转链表后，输出新链表的表头。
'''
def solution(head):
     if head==None or head.next==None:
          return head
     p1=head
     p2=None
     while p1:
          p3=p1.next
          p1.next=p2
          p2=p1
          p1=p3
     return p2
          