# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:56:07 2019

@author: Tang
"""

'''
题目描述



实现一个算法，删除单向链表中间的某个结点，假定你只能访问该结点。 

给定待删除的节点，请执行删除操作，若该节点为尾节点，返回false，否则返回true 
'''
def solution(pnode):
     if pnode.next==None:
          return False
     pnode.val = pnode.next.val
     pnode.next=pnode.next.next
     return True