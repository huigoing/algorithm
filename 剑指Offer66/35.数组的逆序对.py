# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:55:42 2019

@author: Tang
"""

'''
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求
出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。即输出P%1000000007

输入描述:
题目保证输入的数组中没有的相同的数字

数据范围：

	对于%50的数据,size<=10^4

	对于%75的数据,size<=10^5

	对于%100的数据,size<=2*10^5

'''
def solution(a):
     
     def guibing(data,start,end,tmp):
          if start==end:
               return 0
          mid=(start+end)//2
          c1=guibing(tmp,start,mid,data)
          c2=guibing(tmp,mid+1,end,data)
          left=start
          right=mid+1
          i=start
          count=0
          while left<=mid and right<=end:
               if data[left]<=data[right]:
                    tmp[i]=data[left]
                    left+=1
               else:
                    tmp[i]=data[right]
                    right+=1
                    count+=mid-left+1
               i+=1
          while left<=mid:
               tmp[i]=data[left]
               i+=1
               left+=1
          while right<=end:
               tmp[i]=data[right]
               i+=1
               right+=1
          return c1+c2+count
     return guibing(a,0,len(a)-1,a)
a=[1,2,3,4,5,6,7,0]
print(solution(a))
print(a)
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     