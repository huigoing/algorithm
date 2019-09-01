# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:00:22 2019

@author: Tang
"""

'''
题目描述



有一组数，对于其中任意两个数组，若前面一个大于后面一个数字，则这两个数字组成一个逆序对。请设计一个高效的算法，计算给定数组中的逆序对个数。

给定一个int数组A和它的大小n，请返回A中的逆序对个数。保证n小于等于5000。

测试样例：
[1,2,3,4,5,6,7,0],8
返回：7
'''
class AntiOrder:
        def count(self, A, n):
        # write code heref 
            self.count=0
            self.sort(A,0,n)
            return self.count
        def merge(self,a,left,mid,right):
            res=[]
            l=left
            r=mid
            while l<mid and r<right:
                if a[l]<a[r]:
                    res.append(a[l])
                    l+=1
                else:
                    res.append(a[r])
                    r+=1
                    self.count+=(mid-l)
            if l<mid:
                res+=a[l:mid]
            if r<right:
                res+=a[r:right]
            a[left:right]=res
            return a
        def sort(self,a,left,right):
            if (right-left)<=1:
                return a
            mid=(left+right)//2
            self.sort(a,left,mid)
            self.sort(a,mid,right)
            self.merge(a,left,mid,right)
        