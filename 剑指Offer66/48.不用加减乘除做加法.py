# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:48:44 2019

@author: Tang
"""

'''
题目描述


写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''
def solution(a,b):
     res=[]
     res.append(a)
     res.append(b)
     return sum(res)
print(solution(1,2))