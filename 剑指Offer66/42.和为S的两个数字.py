# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:03:15 2019

@author: Tang
"""

'''
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。

输出描述:
对应每个测试案例，输出两个数，小的先输出。
'''
def solution(a,s):
     dic=dict()
     res=[]
     min=1000000000000
     for i in range(len(a)):
          print(dic)
          cha=s-a[i]
          #print(cha)
          if a[i] in dic.keys():
               #print(1)
               if min>a[i]*a[dic[a[i]]]:
                    min=a[i]*a[dic[a[i]]]
               res.append((dic[a[i]],i))
          else:
               dic[cha]=i
     print(min)
     return res
print(solution([1,1,3,5],4))
               