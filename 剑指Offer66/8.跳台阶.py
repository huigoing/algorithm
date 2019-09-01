# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:38:12 2019

@author: Tang
"""

'''
题目描述
一只青蛙一次可以跳上1级台阶，
也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''
def tiao(n):
     #a0=1
     a1=1
     a2=2
     while n-2:
          i=a1+a2
          a1=a2
          a2=i
          n-=1
     return i
print(tiao(10))
     