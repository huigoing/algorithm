# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:31:58 2019

@author: Tang
"""

'''
题目描述



在二维平面上，有一些点，请找出经过点数最多的那条线。

给定一个点集vector<point>p和点集的大小n,没有两个点的横坐标相等的情况,请返回一个vector<double>，
代表经过点数最多的那条直线的斜率和截距。</double></point>
'''
def getLine(self, p, n):
        # write code here
        m=0
        res=[]
        dic=dict()
        for i in range(0,n-1):
            k=(p[i].y-p[i+1].y)/(p[i].x-p[i+1].x)
            b=p[i].y-k*p[i].x
            if (k,b) in dic:
                dic[(k,b)]+=1
            else:
                dic[(k,b)]=1
            #res.append((k,b))
        for i in dic:
            if dic[i]>m:
                m=dic[i]
                res=i
        #rr = collections.Counter(res)
        #return rr.most_common(1)[0][0]           
        return res