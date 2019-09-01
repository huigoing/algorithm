# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:05:43 2019

@author: Tang
"""

'''
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''
def solution(a):
     res=[]
     for i in a:
          if i in res:
               res.remove(i)
          else:
               res.append(i)
     return res
print(solution([2,3,4,1,2,4,1,0]))