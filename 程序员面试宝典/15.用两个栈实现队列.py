# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:52:08 2019

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
     def push(self,data):
          self.stack1.append(data)
     def pop(self):
          if len(self.stack2)==0:
               while self.stack1:
                    self.stack2.append(self.stack1.pop())
          return self.stack2.pop()