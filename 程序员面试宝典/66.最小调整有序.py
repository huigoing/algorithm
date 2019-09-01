# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:57:58 2019

@author: Tang
"""

'''
题目描述



有一个整数数组，请编写一个函数，找出索引m和n，只要将m和n之间的元素排好序，整个数组就是有序的。注意：n-m应该越小越好，也就是说，找出符合条件的最短序列。

给定一个int数组A和数组的大小n，请返回一个二元组，代表所求序列的起点和终点。(原序列位置从0开始标号,若原序列有序，返回[0,0])。保证A中元素均为正整数。

测试样例：
[1,4,6,5,9,10],6
返回：[2,3]
'''
def findSegment(A, n):
        # write code here
        a=sorted(A)
        left=0
        right=n-1
        if a==A:
            return [0,0]
        while left<n:
            if a[left]!=A[left]:
                break
            left+=1
        while right>=0:
            if a[right]!=A[right]:
                break
            right-=1
        return [left,right]


s='the sky is            blue!'
a=[]
for i in range(len(s)-1):
	if s[i]==' ' and s[i+1]==' ':
         flag1=i
         break
    
       
for j in range(flag1+1,len(s)):
	if s[j]!=' ':
         flag2=j
         break
a=s[:flag1]
a=a.split(' ')
print(a)
n=len(a)-1
for i in range(n):
     a[i],a[n-i] = a[n-i], a[i]
print(a)
a=' '.join(a)
print(a)
print(s[flag2:] +' '+a)













