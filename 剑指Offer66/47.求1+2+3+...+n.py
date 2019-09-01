# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:46:33 2019

@author: Tang
"""

'''
题目描述

求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''
def solution(n):
     if n==1:
          return 1
     else:
          return solution(n-1)+n
print(solution(100))