# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:54:15 2019

@author: Tang
"""

'''
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。

输入描述:
输入一个字符串,包括数字字母符号,可以为空

输出描述:
如果是合法的数值表达则返回该数字，否则返回0
 示例1 

输入
复制 
+2147483647
    1a33


输出
复制 
2147483647
    0
'''
def solution(s):
     if len(s)==0 or s=='+' or s=='-':
          return 0
     flag=1
     if s[0]=='-':
          flag=-1
          s=s[1:]
     if s[0]=='+':
          flag=1
          s=s[1:]
     res=[]
     for i in s:
          if i in '1234567890':
               res.append(int(i))
          else:
               return 0
     
     sum=0
     j=len(res)
     for i in res:
          j-=1
          sum+=i*pow(10,j)
     return flag*sum
print(solution('-123'))
          


























