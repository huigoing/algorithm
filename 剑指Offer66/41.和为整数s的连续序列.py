# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:35:12 2019

@author: Tang
"""

'''
题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,
你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''
def solution(k):
     result=[]
     for i in range(1,k+1):
          tmp=[]
          tmp.append(i)
          for j in range(i+1,k+1):
               tmp.append(j)
               if sum(tmp)==k:
                    result.append(tmp)
                    break
               elif sum(tmp)>k:
                    break
               else:
                    pass
     return result
print(solution(100))
