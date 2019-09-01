# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:10:12 2019

@author: Tang
"""

'''
题目描述



请实现一个算法，确定一个字符串的所有字符是否全都不同。这里我们要求不允许使用额外的存储结构。

给定一个string iniString，请返回一个bool值,True代表所有字符全都不同，False代表存在相同的字符。保证字符串中的字符为ASCII字符。字符串的长度小于等于3000。

测试样例：
"aeiou"
返回：True
"BarackObama"
返回：False
'''
def solution(s):
     dic=dict()
     for i in s:
          if i in dic:
               return False
          else:
               dic[i]=1
     return True
print(solution('ABDC'))

def solution2(s):
     return len(set(s))==len(s)
print(solution2('acn'))


a={'a':1,'b':2,'c':3}
for i in a.keys():
     print(a[i] &a[i+1])