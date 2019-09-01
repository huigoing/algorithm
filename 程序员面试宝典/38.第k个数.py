# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:42:51 2019

@author: Tang
"""

'''
题目描述



有一些数的素因子只有3、5、7，请设计一个算法，找出其中的第k个数。

给定一个数int k，请返回第k个数。保证k小于等于100。

测试样例：
3
返回：7
'''
def findKth(k):
        # write code here
        if k==1:
            return 3
        if k==2:
            return 5
        if k==3:
            return 7
        l1=[3,5,7]
        l2=[3,5,7]
        l3=[3,5,7]
        for i in range(3,k):
            m=min(l1[0]*3,l2[0]*5,l3[0]*7)
            if m==l1[0]*3:
                l1.pop(0)
            if m==l2[0]*5:
                l2.pop(0)
            if m==l3[0]*7:
                l3.pop(0)
            l1.append(m)
            l2.append(m)
            l3.append(m)
        return m