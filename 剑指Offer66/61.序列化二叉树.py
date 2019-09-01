# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:13:25 2019

@author: Tang
"""

'''
题目描述


请实现两个函数，分别用来序列化和反序列化二叉树

 1. 对于序列化：使用前序遍历，递归的将二叉树的值转化为字符，并且在每次二叉树的结点
不为空时，在转化val所得的字符之后添加一个' ， '作为分割。对于空节点则以 '#' 代替。
 2. 对于反序列化：按照前序顺序，递归的使用字符串中的字符创建一个二叉树(特别注意：
在递归时，递归函数的参数一定要是char ** ，这样才能保证每次递归后指向字符串的指针会
随着递归的进行而移动！！！)

'''
flag=0
def serialize(root):
     if root==None:
          return '#'
     return str(root.val)+','+serialize(root.left)+','+serialize(root.right)
def deserialize(s):
     l=s.split(',')
     flag+=1
     if flag>=len(s):
          return None
     root=None
     if l[self.flag]!='#':
          root=TreeNode(int(l[self.flag]))
          root.left=self.Deserialize(s)
          root.right=self.Deserialize(s)
     return root