# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:08:54 2019

@author: Tang
"""

'''
题目描述


请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
'''
def solution(s):
     dic=dict()
     for i in s:
          if i in dic:
               dic[i]+=1
          else:
               dic[i]=1
     for i in dic:
          if dic[i]==1:
               return i
     return '#'
