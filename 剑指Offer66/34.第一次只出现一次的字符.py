# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:50:30 2019

@author: Tang
"""

'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 
如果没有则返回 -1（需要区分大小写）.
'''
def solution(s):
     dic=dict()
     for i in s:
          if i in dic:
               dic[i]+=1
          else:
               dic[i]=1
     for i in range(len(s)):
          if dic[s[i]]==1:
               return i
     return -1
