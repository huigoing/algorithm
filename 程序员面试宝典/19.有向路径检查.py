# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:31:04 2019

@author: Tang
"""

'''
题目描述



对于一个有向图，请实现一个算法，找出两点之间是否存在一条路径。 

给定图中的两个结点的指针DirectedGraphNode* a, DirectedGraphNode* b(请不要在意数据类型，图是有向图),
请返回一个bool，代表两点之间是否存在一条路径(a到b或b到a)。 

'''
def solution(a,b):
     def des(a,b,res):
          if a==b:
               return True
          for i in a.neighbors:
               if i not in res:
                    res.add(i)
                    dfs(i,b,res)
          return False
     res=set()
     if a==b:
          return True
     return dfs(a,b,res) or dfs(b,a,res)