# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:15:17 2019

@author: Tang
"""

'''
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变
'''
def solution(a):
     a1=[]
     a2=[]
     for i in a:
          if i%2==1:
               a1.append(i)
          else:
               a2.append(i)
     return a1+a2
a=[1,2,3,4,5,6,7,8]
print(solution(a))
     