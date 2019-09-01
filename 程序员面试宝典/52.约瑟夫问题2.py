# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:39:10 2019

@author: Tang
"""

'''
题目描述



约瑟夫问题是一个著名的趣题。这里我们稍稍修改一下规则。有n个人站成一列。并从头到尾给他们编号，第一个人编号为1。然后从头开始报数，第一轮依次报1，2，1，2...然后报到2的人出局。接着第二轮再从上一轮最后一个报数的人开始依次报1，2，3，1，2，3...报到2，3的人出局。以此类推直到剩下以后一个人。现在需要求的即是这个人的编号。

给定一个int n，代表游戏的人数。请返回最后一个人的编号

测试样例：
5
返回：5
'''
def solution(n):
     res=[i for i in range(1,n+1)]
     step=2
     while len(res)>1:
          res=res[::step]
          step+=1
          res=[res[-1]]+res[:-1]
     return res[0]
a='yong'
print(''.join(sorted(a)))
          