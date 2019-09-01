# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:26:55 2019

@author: Tang
"""

'''
算法简介

   哈希表就是一种以键-值(key-indexed) 存储数据的结构，只要输入待查找的值即key，即可查找到其对应的值。

算法思想

    哈希的思路很简单，如果所有的键都是整数，那么就可以使用一个简单的无序数组来实现：将键作为索引，
    值即为其对应的值，这样就可以快速访问任意键的值。这是对于简单的键的情况，我们将其扩展到可以处理更
    加复杂的类型的键。

算法流程

　　1）用给定的哈希函数构造哈希表；
　　2）根据选择的冲突处理方法解决地址冲突；
　　　　 常见的解决冲突的方法：拉链法和线性探测法。
　　3）在哈希表的基础上执行哈希查找。

复杂度分析

　　单纯论查找复杂度：对于无冲突的Hash表而言，查找复杂度为O(1)（注意，在查找之前我们需要构建相应
  的Hash表）。
'''
# 忽略了对数据类型，元素溢出等问题的判断。
 
class HashTable:
  def __init__(self, size):
    self.elem = [None for i in range(size)] # 使用list数据结构作为哈希表元素保存方法
    self.count = size # 最大表长
 
  def hash(self, key):
    return key % self.count # 散列函数采用除留余数法
 
  def insert_hash(self, key):
    """插入关键字到哈希表内"""
    address = self.hash(key) # 求散列地址
    while self.elem[address]: # 当前位置已经有数据了，发生冲突。
      address = (address+1) % self.count # 线性探测下一地址是否可用
    self.elem[address] = key # 没有冲突则直接保存。
 
  def search_hash(self, key):
    """查找关键字，返回布尔值"""
    star = address = self.hash(key)
    while self.elem[address] != key:
      address = (address + 1) % self.count
      if not self.elem[address] or address == star: # 说明没找到或者循环到了开始的位置
        return False
    return True
 
 
if __name__ == '__main__':
  list_a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
  hash_table = HashTable(12)
  for i in list_a:
    hash_table.insert_hash(i)
  print('hash_table.elem ',hash_table.elem)
 
  for i in hash_table.elem:
    if i:
      print((i, hash_table.elem.index(i)), end=" ")
  print("\n")
 
  print(hash_table.search_hash(15))
  print(hash_table.search_hash(33))
