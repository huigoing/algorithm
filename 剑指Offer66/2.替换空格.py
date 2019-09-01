# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:13:47 2019

@author: Tang
"""

'''
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”
。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
def tihuan(s):
     res=''
     for i in s:
          if i==' ':
               res+='%20'
          else:
               res+=i
     return res
s='we are happy'
print(tihuan(s))