# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:51:34 2019

@author: Tang
"""
'''
题目描述



请实现一种数据结构SetOfStacks，由多个栈组成，其中每个栈的大小为size，
当前一个栈填满时，新建一个栈。该数据结构应支持与普通栈相同的push和pop操作。

给定一个操作序列int[][2] ope(C++为vector&ltvector&ltint>>)，每个操作的第一
个数代表操作类型，若为1，则为push操作，后一个数为应push的数字；若为2，则为pop操作，
后一个数无意义。请返回一个int[][](C++为vector&ltvector&ltint>>)，为完成所有操作后的SetOfStacks，
顺序应为从下到上，默认初始的SetOfStacks为空。保证数据合法。
'''
def setOfStacks(self, ope, size):
        # write code here
        result=[[]]
        for i in ope:
            if i[0]==1:
                if len(result[-1])==size:
                    result.append([])
                result[-1].append(i[1])
            if i[0]==2:
                if len(result[-1])==0:
                    result.pop()
                result[-1].pop()
        return result