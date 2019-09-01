# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:51:04 2019

@author: Tang
"""
'''
题目描述


请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，
字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。


?  匹配一个字符0次或1次

+  匹配前一个字符1次或无限次
 
*  匹配前一个字符0或多次
 
 
'''
import re
def isNumeric(s):
        # write code here
        m=re.compile("[+-]?[0-9]*([.][0-9]*)?([eE][+-]?[0-9]+)?")
        if re.match(m,s).group()==s:return True
        else:return False
print(isNumeric('-.e+1'))