# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:31:44 2019

@author: Tang
"""

'''
题目描述



有一堆箱子，每个箱子宽为wi，长为di，高为hi，现在需要将箱子都堆起来，而且为了使堆起来的箱子不倒，上面的箱子的宽度和长度必须小于下面的箱子。请实现一个方法，求出能堆出的最高的高度，这里的高度即堆起来的所有箱子的高度之和。 

给定三个int数组w,l,h，分别表示每个箱子宽、长和高，同时给定箱子的数目n。请返回能堆成的最高的高度。保证n小于等于500。 

测试样例： 
[1,1,1],[1,1,1],[1,1,1]
返回：1
'''
def getHeight( w, l, h, n):
        # write code here
        box=[[i,j,z] for i,j,z in zip(w,l,h)]
        res=[0 for i in range(n)]
        box = sorted(box)[::-1]
        tmp=0
        for i in range(n):
            res[i]=box[i][2]
            for j in range(i):
                if box[j][0] > box[i][0] and box[j][1] > box[i][1]:
                    res[i]=max(res[i],res[j]+box[i][2])
            tmp=max(tmp,res[i])
        return tmp