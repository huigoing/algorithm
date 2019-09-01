# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:21:00 2019

@author: Tang
"""

'''
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
def solution(a):
     if len(a)==0:
          return False
     if len(a)==1:
          return True
     root=a[-1]
     left=0
     while a[left]<root:
          left+=1
     for i in range(left,len(a)-1):
          if a[i]<root:
               return False
     return solution(a[:left]) or solution(a[left:len(a)-1])
print(solution([4,1,3,7]))