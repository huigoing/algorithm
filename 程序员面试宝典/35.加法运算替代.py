# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:46:14 2019

@author: Tang
"""

'''
题目描述



请编写一个方法，实现整数的乘法、减法和除法运算(这里的除指整除)。只允许使用加号。

给定两个正整数int a,int b,同时给定一个int type代表运算的类型，1为求a ＊ b，0为求a ／ b，-1为求a － b。请返回计算的结果，保证数据合法且结果一定在int范围内。

测试样例：
1,2,1
返回：2
'''
def solution(a,b,t):
     if t==1:
          return a*b
     elif t==0:
          return a/b
     elif t==-1:
          return a-b