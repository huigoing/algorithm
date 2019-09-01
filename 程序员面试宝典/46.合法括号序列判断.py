# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:39:04 2019

@author: Tang
"""
'''
题目描述



对于一个字符串，请设计一个算法，判断其是否为一个合法的括号串。

给定一个字符串A和它的长度n，请返回一个bool值代表它是否为一个合法的括号串。

测试样例：
"(()())",6
返回：true

测试样例：
"()a()()",7
返回：false

测试样例：
"()(()()",7
返回：false
'''
def chkParenthesis( A, n):
        # write code here
        if n%2!=0:
            return False
        if A[0]=='(':
            stack=[A[0]]
        else:
            return False
        i=1
        while i<n:
            print(111)
            if A[i]=="(":
                stack.append(A[i])
            elif A[i]==")":
                if stack:
                    stack.pop(-1)
                else:
                    return False
            else:
                return False
            i+=1
        return True

print(chkParenthesis("()))))()(d",10))