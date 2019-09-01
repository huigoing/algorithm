# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:42:41 2019

@author: Tang
"""

'''
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
            | 1       ,(n=0 )  

f(n) =     | 1       ,(n=1 ) 

           | 2*f(n-1),(n>=2)
'''
def tiao(n):
     if n<=0:
          return -1
     elif n==1:
          return 1
     else:
          return 2*tiao(n-1)
print(tiao(3))
     