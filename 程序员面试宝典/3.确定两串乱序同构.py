# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:33:30 2019

@author: Tang
"""

'''
题目描述



给定两个字符串，请编写程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
这里规定大小写为不同字符，且考虑字符串中的空格。 

给定一个string stringA和一个string stringB，请返回一个bool，代表两串是否重新排列后可相同。
保证两串的长度都小于等于5000。 

测试样例： 
"This is nowcoder","is This nowcoder"
返回：true
"Here you are","Are you here"
返回：false
'''
def solution1(sa,sb):
     if len(sa)!=len(sb):
          return False
     return set(sa)==set(sb)

def solution2(sa,sb):
     dic=dict()
     if len(sa)!=len(sb):
          return False
     for i in sa:
          if i in dic:
               dic[i]+=1
          else:
               dic[i]=1
     for i in sb:
          if  i not in dic :
               return False
          elif  dic[i]<=0:
               return False
          else:
               dic[i]-=1
     return True
     