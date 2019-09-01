# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:09:58 2019

@author: Tang
"""

def maxInWindows(num, size):
        def kuaipai(a,start,end):
             if start<end:
                 l=start
                 r=end
                 tmp=a[l]
                 while l<r:
                     while l<r and a[r]>tmp:
                         r-=1
                     if l<r:
                         a[l]=a[r]
                     while l<r and a[l]<=tmp:
                         l+=1
                     if l<r:
                         a[r]=a[l]
                 a[l]=tmp
                 kuaipai(a,start,l-1)
                 kuaipai(a,l+1,end)
        #kuaipai(num,0,len(num)-1)
        print(num)
        if len(num)==0 or len(num)<size or size==0:
            return []
        #m=float('-inf')
        res=[]
        for i in range(0,len(num)-size+1):
            #m=max(num[i:i+size])
            a=num[i:i+size]
            kuaipai(a,0,size-1)
            res.append(a[-1])
            #i+=size
        return res
        # write code here
        
print(maxInWindows([2,3,4,2,6,2,5,1],3))