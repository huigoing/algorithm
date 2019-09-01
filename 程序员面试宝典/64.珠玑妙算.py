# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:02:16 2019

@author: Tang
"""

'''
题目描述



我们现在有四个槽，每个槽放一个球，颜色可能是红色(R)、黄色(Y)、绿色(G)或蓝色(B)。例如，可能的情况为RGGB(槽1为红色，槽2、3为绿色，槽4为蓝色)，作为玩家，你需要试图猜出颜色的组合。比如，你可能猜YRGB。要是你猜对了某个槽的颜色，则算一次“猜中”。要是只是猜对了颜色但槽位猜错了，则算一次“伪猜中”。注意，“猜中”不能算入“伪猜中”。

给定两个string A和guess。分别表示颜色组合，和一个猜测。请返回一个int数组，第一个元素为猜中的次数，第二个元素为伪猜中的次数。

测试样例：
"RGBY","GGRR"
返回：[1,1]
'''
def calcResult( A, guess):
        # write code here
        res=[]
        a=[]
        b=[]
        s=0
        ss=0
        for i in range(len(A)):
            if A[i]==guess[i]:
                s+=1
            else:
                a.append(A[i])
                b.append(guess[i])
        res.append(s)
        for i in a:
            if i in b:
                b.remove(i)
                ss+=1
        res.append(ss)
        return res