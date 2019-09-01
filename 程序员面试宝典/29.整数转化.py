# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:16:45 2019

@author: Tang
"""

'''
题目描述



编写一个函数，确定需要改变几个位，才能将整数A转变成整数B。 

给定两个整数int A，int B。请返回需要改变的数位个数。 

测试样例： 
10,5
返回：4
'''
def solution(a,b):
     a=a^b#异或
     count=0
     while a:
          count+=1
          a=a&(a-1)#每次减少一个1
     return count
     