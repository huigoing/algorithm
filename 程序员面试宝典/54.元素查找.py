# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:11:13 2019

@author: Tang
"""

'''
题目描述



有一个排过序的数组，包含n个整数，但是这个数组向左进行了一定长度的移位，例如，原数组为[1,2,3,4,5,6]，向左移位5个位置即变成了[6,1,2,3,4,5],现在对于移位后的数组，需要查找某个元素的位置。请设计一个复杂度为log级别的算法完成这个任务。

给定一个int数组A，为移位后的数组，同时给定数组大小n和需要查找的元素的值x，请返回x的位置(位置从零开始)。保证数组中元素互异。

测试样例：
[6,1,2,3,4,5],6,6
返回：0
'''
def solution(a,x):
     l=0
     r=len(a)-1
     while l<=r:
          m=(l+r)//2
          if a[m]==x:
               return True
          elif x>a[m]:
               if a[m]<a[r] and a[r]<x:
                    r=m-1
               else:
                    l=m+1
          else:
               if a[m]>a[l] and a[l]>x:
                    l=m-1
               else:
                    r=m+1
     return False
                    
                    
                    
                    
                    
                    