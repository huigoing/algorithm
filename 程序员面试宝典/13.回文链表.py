# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:36:20 2019

@author: Tang
"""

'''
题目描述



请编写一个函数，检查链表是否为回文。

给定一个链表ListNode* pHead，请返回一个bool，代表链表是否为回文。

测试样例：
{1,2,3,2,1}
返回：true
{1,2,3,2,3}
返回：false
'''
def solution(head):
     res=[]
     p=head
     if p==None:
          return False
     while p:
          res.append(p.val)
          p=p.next
     for i in range(len(res)):
          if res[i]!=res[len(res)-1-i]:
               return False
     return True