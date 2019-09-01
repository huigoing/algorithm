# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:57:57 2019

@author: Tang
"""

'''
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，
]则打印出这三个数字能排成的最小数字为321323。
'''
import functools
def solution(numbers):
     def compare1(x, y):
        if x+y > y+x:
            return 1
        if x+y < y+x:
            return -1
        return 0
     if not numbers:
            return ''
     strnum = [str(numbers[i]) for i in range(len(numbers))]
     strnum=sorted(strnum,key=functools.cmp_to_key(compare1))
     return int(''.join(strnum))
    

print(solution([3,32,321]))