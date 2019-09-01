# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:37:19 2019

@author: Tang
"""

'''
题目描述
统计一个数字在排序数组中出现的次数。
'''
def solution(a,n):
     dic=dict()
     for i in a:
          if i in dic[i]:
               dic[i]+=1
          else:
               dic[i]=1
     if n in dic:
          return dic[n]
     else:
          return 0
     
     