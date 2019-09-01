# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:30:40 2019

@author: Tang
"""

'''
题目描述



编写代码，以给定值x为基准将链表分割成两部分，所有小于x的结点排在大于或等于x的结点之前

给定一个链表的头指针 ListNode* pHead，请返回重新排列后的链表的头指针。注意：
分割以后保持原来的数据顺序不变。
'''
def solution(head,k):
     if head==None:
          return head
     left=p=ListNode(0)
     right=q=ListNode(0)
     while head:
          if head.val<k:
               p.next=head
               p=p.next
          else:
               q.next=head
               q=q.next
          head=head.next
     q.next=None
     p.next=right.next
     return left.next
