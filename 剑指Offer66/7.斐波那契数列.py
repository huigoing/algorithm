# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:30:52 2019

@author: Tang
"""

'''
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0）。 
n<=39 
'''
def find(n):
     a1=1
     a2=1
     if n==0:
          return 0
     if n<=2:
          return a1
     while n-2:
          tmp=a1
          a1=a2
          a2=tmp+a1
          n-=1
     return a2
print(find(50))