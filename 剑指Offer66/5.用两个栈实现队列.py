# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:38:11 2019

@author: Tang
"""

'''
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
class solution():
     def __init__(self):
          self.stack1=[]
          self.stack2=[]
     def push(self,a):
          self.stack1.append(a)
     def pop(self):
          if len(self.stack2)==0:
               while self.stack1:
                    tmp=self.stack1.pop(-1)
                    self.stack2.append(tmp)
          return self.stack2.pop()
a=solution()
a.push(2)
print(a.pop())
