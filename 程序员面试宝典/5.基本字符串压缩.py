# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:15:20 2019

@author: Tang
"""

'''
题目描述



利用字符重复出现的次数，编写一个方法，实现基本的字符串压缩功能。比如，字符串“aabcccccaaa”经压缩
会变成“a2b1c5a3”。若压缩后的字符串没有变短，则返回原先的字符串。

给定一个string iniString为待压缩的串(长度小于等于10000)，保证串内字符均由大小写英文字母组成，
返回一个string，为所求的压缩后或未变化的串。

测试样例
"aabcccccaaa"
返回："a2b1c5a3"
"welcometonowcoderrrrr"
返回："welcometonowcoderrrrr
'''
def solution(s):
     res=''
     count=1
     for i in range(len(s)-1):
          if s[i+1]==s[i]:
               count+=1
          else:
               count=1
               res+=s[i]+str(count)
     res+=s[-1]+str(count)
     if len(s)<=len(res):
          return s
     else:
          return res
               