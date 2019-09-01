# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:36:48 2019

@author: Tang
"""

'''
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
 '''
def solution(n):
      if n<1:
           return 0
      i1=0
      i2=0
      i3=0
      data=[1]
      i=1
      while i<n:
           tmp = min(data[i1]*2,data[i2]*3,data[i3]*5)
           data.append(tmp)
           while data[i1]*2<=tmp:
                i1+=1
           while data[i2]*3<=tmp:
                i2+=1
           while data[i3]*5<=tmp:
                i3+=1
           i+=1
           print(data)
      return data[n-1]
print(solution(7))
      
      