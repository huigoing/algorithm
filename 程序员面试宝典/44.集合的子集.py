# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 16:43:29 2019

@author: Tang
"""

'''
题目描述



请编写一个方法，返回某集合的所有非空子集。 

给定一个int数组A和数组的大小int n，请返回A的所有非空子集。保证A的元素个数小于等于20，且元素互异。
各子集内部从大到小排序,子集之间字典逆序排序，见样例。 

测试样例： 
[123,456,789]
返回：{[789,456,123],[789,456],[789,123],[789],[456 123],[456],[123]}
'''
def solution(A,n):
     res=[]
     A.sort(reverse=True)
     def dfs(A,a):
          if a:
               res.append(a)
          for i in range(len(A)):
               dfs(A[i+1:],a+[A[i]])
     dfs(A,[])
     res.sort(reverse=True)
     return res