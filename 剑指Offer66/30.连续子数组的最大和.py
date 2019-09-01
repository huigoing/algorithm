# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:27:14 2019

@author: Tang
"""

'''
题目描述
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:
     在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
     但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
     例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
     给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
'''
def solution(a):
     current=a[0]
     maxnum=a[0]
     start=0
     end=0
     for i in range(1,len(a)):
          if current>0:
               current+=a[i]
               
          else:
               start=i
               current=a[i]
          if current>maxnum:
               maxnum=current
               end=i
     print(start,end)
     print(a[start:end])
     return maxnum
a=[6,-3,-2,7,-15,1,2,2]
print(solution(a))



def other(a):
     maxnum=a[0]
     for i in range(len(a)):
          current=0
          for j in range(i,len(a)):
               current+=a[j]
               if current>maxnum:
                    maxnum=current
                    start=i
                    end=j
     print(maxnum,a[start:end+1])
other(a)
                    
               
               
               
               
               
               
               
               