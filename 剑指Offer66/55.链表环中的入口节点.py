# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:11:46 2019

@author: Tang
"""

'''
题目描述


给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''
def solution(head):
     slow=head
     fast=head
     if head ==None or head.next==None:
          return None
     while fast and fast.next:
          fast=fast.next.next
          slow=slow.next
          if fast==slow:
               #break
               slow=head
               while slow!=fast:
                    slow=slow.next
                    fast=fast.next
               if slow==fast:
                    return slow
     return None
          