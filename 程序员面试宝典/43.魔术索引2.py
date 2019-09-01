# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 16:16:24 2019

@author: Tang
"""

'''
题目描述



在数组A[0..n-1]中，有所谓的魔术索引，满足条件A[i]=i。给定一个不下降序列，元素值可能相同，
编写一个方法，判断在数组A中是否存在魔术索引。请思考一种复杂度优于o(n)的方法。

给定一个int数组A和int n代表数组大小，请返回一个bool，代表是否存在魔术索引。

测试样例：
[1,1,3,4,5]
返回：true

解析
应该是从i：0~n - 1进行遍历，如果当前A[i] == i，返回true；如果A[i] < i， 则i++；如果A[i] > i，
则令i = A[i]，即跳过A[i] - i个元素（因为序列是非递减的，所以A[i] >i时，至少到i = A[i]处，
才有可能出现A[i] == i）。 

例如2， 2， 2， 4， 5序列，i == 0时，A[i] = 2，则应跳过i = 1，直接比较i = 2处
'''
def solution(A,n):
        i=0
        while i<n:
            if A[i]==i:
                return True
            elif A[i]<i:
                i+=1
            else:
                i=A[i]
        return False
print('d'+'d')