# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:50:20 2019

@author: Tang
"""

'''
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
def solution(n):
     count=0
     if n<0:
          n=n&0xffffffff
     while n:
          n=n&(n-1)
          count+=1
     return count
print(solution(-1))