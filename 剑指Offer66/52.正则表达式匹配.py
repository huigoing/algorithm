# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:01:00 2019

@author: Tang
"""

'''
题目描述


请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配


当模式中的第二个字符不是“*”时： 

1、如果字符串第一个字符和模式中的第一个字符相匹配，那么字符串和模式都后移一个字符，然后匹配剩余的。 

2、如果 字符串第一个字符和模式中的第一个字符相不匹配，直接返回false。 


 

而当模式中的第二个字符是“*”时： 

如果字符串第一个字符跟模式第一个字符不匹配，则模式后移2个字符，继续匹配。如果字符串第一个字符跟模式第一个字符匹配，可以有3种匹配方式： 

1、模式后移2字符，相当于x*被忽略； 

2、字符串后移1字符，模式后移2字符； 

3、字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位； 


'''
def solution(a,b):
     if len(a)>0 and len(b)==0:
          return False
     if len(a)==0 and len(b)==0:
          return True
     if len(b)>1 and b[1]=='*':
          if len(a)>0 and (a[0]==b[0] or b[0]=='.'):
               #             0次             大于1次                      1次
               return solution(a,b[2:]) or solution(a[1:],b) or solution(a[1:],b[2:])
          else:
               return solution(a,b[2:])
     if a and (a[0]==b[0] or b[0]=='.'):
          return solution(a[1:],b[1:])
     return False
print(solution('aaa','a*a'))