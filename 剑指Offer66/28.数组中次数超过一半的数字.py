# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:49:38 2019

@author: Tang
"""

'''
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
超过数组长度的一半，因此输出2。如果不存在则输出0
'''
def solution(a):
     dic=dict()
     for i in a:
          if i in dic:
               dic[i]+=1
               if dic[i]>len(a)//2:
                    return i
          else:
               dic[i]=1
    
     return 0
a=[1,2,3,2,2,2,5,4,2]
print(solution(a))