# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:56:30 2019

@author: Tang
"""

'''
题目描述 考的排序
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''
def solution(a,k):
     def kuaipai(a,start,end):
          if start<end:

               flag=a[start]
               left=start
               right=end
               #print(a)
               while left<right:
                    while left<right and a[right]>flag:
                         right-=1
                    if left<right:
                         a[left]=a[right]
                         left+=1
                    
                    while left<right and a[left]<flag:
                         left+=1
                    if left<right:
                         a[right]=a[left]
                         right-=1
               a[left]=flag
               kuaipai(a,start,left-1)
               kuaipai(a,left+1,end)
     if len(a)<k or k<0 or len(a)==0:
          return []
     kuaipai(a,0,len(a)-1)
     print(a)
     print(a[:k])
     
a=[4,5,1,6,2,7,3,8]
solution(a,4)