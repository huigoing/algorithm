# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:42:28 2019

@author: Tang
"""

'''
题目描述



对于一个元素各不相同且按升序排列的有序序列，请编写一个算法，创建一棵高度最小的二叉查找树。

给定一个有序序列int[] vals,请返回创建的二叉查找树的高度。
'''
def solution(data):
     l=len(data)
     if l<=2:
          return l
     left=0
     right=l
     mid=(left+right)//2
     p=solution(data[:mid])
     q=solution(data[mid+1:])
     if p>q:
          return p+1
     else:
          return q+1
     
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(solution(a))
s=input()
print(s)