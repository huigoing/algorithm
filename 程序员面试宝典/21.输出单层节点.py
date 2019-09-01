# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:34:58 2019

@author: Tang
"""

'''
题目描述



对于一棵二叉树，请设计一个算法，创建含有某一深度上所有结点的链表。

给定二叉树的根结点指针TreeNode* root，以及链表上结点的深度，请返回一个链表ListNode，
代表该深度上所有结点的值，请按树上从左往右的顺序链接，保证深度不超过树的高度，
树上结点的值为非负整数且不超过100000。
'''
def solution(root,dep):
     res=[root]
     count=1
     while dep:
          dep-=1
          tmp=0
          while count:
               x=res.pop(0)
               if x.left:
                    res.append(x.left)
                    tmp+=1
               if x.right:
                    res.append(x.right)
                    tmp+=1
               count-=1
          count=tmp
     head=ListNode(-1)
     p=head
     for i in res:
          p.next=ListNode(i.val)
          p=p.next
     return head.next