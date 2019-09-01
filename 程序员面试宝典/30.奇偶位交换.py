# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:30:32 2019

@author: Tang
"""

'''
题目描述



请编写程序交换一个数的二进制的奇数位和偶数位。（使用越少的指令越好）

给定一个int x，请返回交换后的数int。

测试样例：
10
返回：5


用0xAAAAAAAA与x相与求的奇数位上数字(偶数位上数字为0) 

用0x 55555555 与x相与求的偶数位上数字(奇数位上数字为0) 


 

oddVal右移一位 even左移一位  相加即可。 

'''
def solution(x):
     a=x&0xaaaaaaaa
     b=x&0x55555555
     return a>>1 | b<<1