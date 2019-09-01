# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:21:57 2019

@author: Tang
"""
import time
#被装饰的函数带参数
def get_time3(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        processTime = (endTime - startTime) * 1000
        print ("The function timing is %f ms" %processTime)
    return wrapper
@ get_time3
def myfunc2(a):
    print ("start func")
    print(a)
    time.sleep(0.8)
    print ("end func")

a = "test"
print('name is ',myfunc2.__name__)
myfunc2(a)