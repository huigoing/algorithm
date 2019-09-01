# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:01:03 2019

@author: Tang
"""

'''
题目描述



请编写一个程序，按升序对栈进行排序（即最大元素位于栈顶），要求最多只能使用一个额外的栈存放临时数据，
但不得将元素复制到别的数据结构中。 

给定一个int[] numbers(C++中为vector&ltint>)，其中第一个元素为栈顶，请返回排序后的栈。
请注意这是一个栈，意味着排序过程中你只能访问到最后一个元素。 

测试样例： 
[1,2,3,4,5]
返回：[5,4,3,2,1]
'''
def solution(data):
     if len(data)==0:
          return []
     res=[]
     while data:
          tmp=data.pop()
          while res and res[-1]<tmp:
               data.append(res.pop())
          res.append(tmp)
     return res

a=[1,1,-1]
a.remove(-1)
print(a)