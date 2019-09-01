# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:55:15 2019

@author: Tang
"""

'''
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''
def solution(base,exponent):
     result=1
     if exponent>0:
          while exponent:
               result*=base
               exponent-=1
          return result
     elif exponent==0:
          return 1
     else:
          n=abs(exponent)
          print(n)
          while n:
               result*=base
               n-=1
          return 1/result
               
     #return result
print(solution(2,-4))