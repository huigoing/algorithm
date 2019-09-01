# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:00:27 2019

@author: Tang
"""

'''
题目描述



请编写一个方法，对一个字符串数组进行排序，将所有变位词合并，保留其字典序最小的一个串。这里的变位词指变换其字母顺序所构成的新的词或短语。例如"triangle"和"integral"就是变位词。

给定一个string的数组str和数组大小int n，请返回排序合并后的数组。保证字符串串长小于等于20，数组大小小于等于300。

测试样例：
["ab","ba","abc","cba"]
返回：["ab","abc"]
'''
def solution(s):
     dic=dict()
     for i in s:
          tmp=''.join(sorted(i))
          if tmp not in dic:
               dic[tmp]=i
          elif i<dic[tmp]:
               dic[tmp]=i
     a=[]
     for i in dic:
          a.append(dic[i])
     return sorted(a)