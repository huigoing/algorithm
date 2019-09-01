# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:37:51 2019

@author: Tang
"""

'''
算法简介

    二分查找（Binary Search），是一种在有序数组中查找某一特定元素的查找算法。
    查找过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则查找过程结束；
    如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，
    而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。
    这种查找算法每一次比较都使查找范围缩小一半。

算法描述 

    给予一个包含 n个带值元素的数组A 


        1、 令 L为0 ， R为 n-1 ；
        2、 如果L>R，则搜索以失败告终 ；
        3、 令 m (中间值元素)为  ⌊(L+R)/2⌋；
        4、 如果 Am<T，令 L为 m + 1 并回到步骤二 ；
        5、 如果 Am>T，令 R为 m - 1 并回到步骤二；

复杂度分析 

    时间复杂度：折半搜索每次把搜索区域减少一半，时间复杂度为 O(logn) 
    空间复杂度：O(1)
'''
def binary_search(lis, key):
  low = 0
  high = len(lis) - 1
  time = 0
  while low < high:
    time += 1
    mid = int((low + high) // 2)
    if key < lis[mid]:
      high = mid - 1
    elif key > lis[mid]:
      low = mid + 1
    else:
      # 打印折半的次数
      print("times: %s" % time)
      return mid
  print("times: %s" % time)
  return False
 
if __name__ == '__main__':
  LIST = [1, 5, 7, 8, 22, 54, 99,123, 200, 222, 444]
  result = binary_search(LIST, 99)
  print(result)



























