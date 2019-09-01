# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:53:15 2019

@author: Tang
"""

'''
有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶、3阶。请实现一个方法，
计算小孩有多少种上楼的方式。为了防止溢出，请将结果Mod 1000000007 

给定一个正整数int n，请返回一个数，代表上楼的方式数。保证n小于等于100000。 

'''
def countWays( n):
        # write code here
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 4
        n1,n2,n3=1,2,4
        for i in range(3,n):
            tmp=(n1+n2+n3)%1000000007 
            n1=n2
            n2=n3
            n3=tmp
        return n3