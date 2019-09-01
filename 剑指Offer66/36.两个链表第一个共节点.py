# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:29:57 2019

@author: Tang
"""

'''
输入两个链表，找出它们的第一个公共结点。
'''
def solution(head1,head2):
     res=[]
     if head1==None and head2==None:
          return None
     while head1:
          res.append(head1.val)
          head1=head1.next
     while head2:
          if head2.val in res:
               return head2
          head2=head2.next
     return None
     