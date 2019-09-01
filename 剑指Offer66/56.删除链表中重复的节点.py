# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:44:16 2019

@author: Tang
"""

'''
题目描述


在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''
def solution1(head):
     dic=dict()
     if head==None:
          return None
     res=[]
     while head:
          res.append(head.val)
          head=head.next
     for i in res:
          if i in dic:
               dic[i]+=1
          else:
               dic[i]=1
     dummy=ListNode(0)
     p=dummy
     for i in dic:
          if dic[i]==1:
               p.next=ListNode(i)
               p=p.next
     return dummy.next

def solution2(head):
     if head==None:
          return None
     dummy=ListNode(0)
     dummy.next=head
     p=dummy
     q=head
     while q and q.next:
          if q.val == q.next.val:
               while q.next and q.val==q.next.val:
                    q=q.next
          else:
               p.next=q
               p=p.next
          q=q.next
     p.next=q
     return dummy.next
          
          
          
          
          
          
          
     














               