# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:42:17 2019

@author: Tang
"""

'''
题目描述



请编写一个方法，找出两个数字中最大的那个。条件是不得使用if-else等比较和判断运算符。 

给定两个int a和b，请返回较大的一个数。若两数相同则返回任意一个。 

测试样例： 
1，2
返回：2
'''
def getMax(a, b):
        # write code here
        c=(a-b)>>31
        return a+c*(a-b)
from collections import Iterable
a=iter([1,2,3])
print(isinstance(a,Iterable))
print(type(a))
print(next(a))
print(map(str, [1,2,3,4,5,6]))
import time


def get_time(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        processTime = (endTime - startTime) * 1000
        print ("The function timing is %f ms" %processTime)
    return wrapper
    

print('====================')
@ get_time
def myfuncrrrrc():
    print ("start func")
    time.sleep(0.8)
    print ("end func")

print ("myfunc is: ", myfunc.__name__)
myfunc()









