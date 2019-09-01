# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:34:55 2019

@author: Tang
"""

'''
题目描述
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字
有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,
并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
'''
def solution(n):
     count=0
     base=1
     tmp=n
     while tmp:
          last=tmp%10
          tmp=int(tmp/10)
          count+=tmp*base
          if last==1:
               count=count+n%base+1
          elif last>1:
               count+=base
          base*=10
     return count
print(solution(111))