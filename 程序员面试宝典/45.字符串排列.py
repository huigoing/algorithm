# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:21:46 2019

@author: Tang
"""

'''
题目描述



编写一个方法，确定某字符串的所有排列组合。

给定一个string A和一个int n,代表字符串和其长度，请返回所有该字符串字符的排列，保证字符串长度小于等于11且字符串中字符均为大写英文字符，排列中的字符串按字典序从大到小排序。(不合并重复字符串)

测试样例：
"ABC"
返回：["CBA","CAB","BCA","BAC","ACB","ABC"]
'''
def solution(A):
     res=[]
     def dfs(A,a):
          if len(A)==0:
               res.append(a)
          for i in range(len(A)):
               dfs(A[:i]+A[i+1:],a+A[i])
     dfs(A,'')
     res.sort(reverse=True)
     return res
a='www'
print(a[0])