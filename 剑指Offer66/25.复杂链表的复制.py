# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:43:14 2019

@author: Tang
"""

'''
题目描述


输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''
def solution(head):
     p=head
     #复制
     while p:
          pclone=RandomListNode(p.val)
          pclone.next=p.next
          p.next=pclone
          p=p.next
     p=head
     while p:
          pclone=p.next
          if p.random!=None:
               pclone.random=p.ramdom.next
          p=pclone.next
     #拆分
     p=head
     pclonehead=None
     pclone=None
     if p.next:
          pclonehead=p.next
          pclone=pclonehead
          p.next=pclone.next
          p=p.next
     while p:
          pclone.next=p.next
          pclone=pclone.next
          p.next=pclone.next
          p=p.next
     return pclonehead
          
     
          