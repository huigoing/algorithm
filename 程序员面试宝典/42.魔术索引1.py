# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:08:13 2019

@author: Tang
"""

'''
题目描述



在数组A[0..n-1]中，有所谓的魔术索引，满足条件A[i]=i。给定一个升序数组，元素值各不相同，编写一个方法，判断在数组A中是否存在魔术索引。请思考一种复杂度优于o(n)的方法。

给定一个int数组A和int n代表数组大小，请返回一个bool，代表是否存在魔术索引。

测试样例：
[1,2,3,4,5]
返回：false
'''
def solution1(A,n):#二分法
        left=0
        right=n
        
        while left<=right:
            mid=(left+right)//2
            res=A[mid]
            if mid<res:
                right=mid-1
            elif mid>res:
                left=mid+1
            else:
                return True
        return False
def solution(A,n):
     for i in range(n):
          if A[i]==i:
               return True
     return False
     
     
     
     
     