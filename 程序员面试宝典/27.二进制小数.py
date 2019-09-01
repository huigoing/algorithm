# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:01:47 2019

@author: Tang
"""

'''
题目描述



有一个介于0和1之间的实数，类型为double，返回它的二进制表示。如果该数字无法精确地用32位以内的二进制表示，返回“Error”。

给定一个double num，表示0到1的实数，请返回一个string，代表该数的二进制表示或者“Error”。

测试样例：
0.625
返回：0.101
'''
def solution(num):
     mystring='0.'
     while num!=0:
          num*=2
          if len(mystring)==32:
               return 'Error'
          if num>=1:
               num-=1
               mystring+='1'
          else:
               mystring+='0'
     return mystring
               