# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:30:50 2019

@author: Tang
"""

'''
题目描述



有一个排过序的字符串数组，但是其中有插入了一些空字符串，请设计一个算法，找出给定字符串的位置。算法的查找部分的复杂度应该为log级别。

给定一个string数组str,同时给定数组大小n和需要查找的string x，请返回该串的位置(位置从零开始)。

测试样例：
["a","b","","c","","d"],6,"c"
返回：3

这是一道二分查找 的变形题目。唯一的关注点就是当str[mid] ==""时的处理，此时仅通过str[mid]=""是无法判断目标是在mid的左边还是右边。所以，我们遍历mid左边的元素找到第一个不是空字符串的元素。 

如果mid左边的所有元素都是空字符串，则去掉令start=mid+1； 

否则 

    找到第一个不是空字符串的元素下标为index 

    （1）如果str[index]等于目标正好返回。 

    （2）如果str[index]大于目标，则说明目标在str[index]左边，令end = index - 1。 

    （3）如果str[index]小于目标，则说明目标在str[mid]右边，令start = mid + 1



'''
def solution(s,x):
        l=0
        r=len(s)-1
        while l<=r:
            m=(l+r)//2
            if s[m]==' ':
                left=m-1
                right=m+1
                while True:
                    if left<l or right>r:
                        return -1
                    elif left>l and s[left]!=' ':
                        m=left
                        break
                    elif right<r and s[right]!=' ':
                        m=right
                        break
                    left-=1
                    right+=1
            if s[m]==x:
                return m
            elif s[m] < x:
                l=m+1
            else:
                r=m-1
        return  -1
     