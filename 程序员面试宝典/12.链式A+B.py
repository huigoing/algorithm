# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:33:07 2019

@author: Tang
"""

'''
题目描述



有两个用链表表示的整数，每个结点包含一个数位。这些数位是反向存放的，
也就是个位排在链表的首部。编写函数对这两个整数求和，并用链表形式返回结果。

给定两个链表ListNode* A，ListNode* B，请返回A+B的结果(ListNode*)。

测试样例：
{1,2,3},{3,2,1}
返回：{4,4,4}
'''
def solution(a,b):
     if a==None and b==None:
          return None
     if a==None:
          return b
     if b==None:
          return a
     p=a
     pp=a
     res=0
     while a and b:
          a.val=a.val+b.val+res
          if a.val>=10:
               res=a.val//10
               a.val=a.val-10
          else:
               res=0
          pp=a
          a=a.next
          b=b.next
     if b:
          pp.next=b
          pp=pp.next
          a=pp
     while a:
          a.val+=res
          if a.val>=10:
               res=a.val//10
               a.val-=10
          else:
               res=0
          pp=a
          a=a.next
     if res:
          tmp=ListNode(res)
          pp.next=tmp
          a=pp
     return p
          
          
          
          
               
               
               
               
               
               
               
               