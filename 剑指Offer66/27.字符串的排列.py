# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:33:10 2019

@author: Tang
"""
'''
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
def solution(s):
     if len(s)==0:
          return []
     def dfs(s,res,tmp):
          if len(s)==0:
               res.add(tmp)
          for i in range(len(s)):
               dfs(s[:i]+s[i+1:],res,tmp+s[i])
     res=set()
     dfs(s,res,'')
     return res
print(solution('abc'))