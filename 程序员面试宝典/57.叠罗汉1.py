# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 15:19:30 2019

@author: Tang
"""

'''
题目描述



叠罗汉是一个著名的游戏，游戏中一个人要站在另一个人的肩膀上。同时我们应该让下面的人比上面的人更高一点。已知参加游戏的每个人的身高，请编写代码计算通过选择参与游戏的人，我们最多能叠多少个人。注意这里的人都是先后到的，意味着参加游戏的人的先后顺序与原序列中的顺序应该一致。 

给定一个int数组men，代表依次来的每个人的身高。同时给定总人数n，请返回最多能叠的人数。保证n小于等于500。 

测试样例： 
[1,6,2,5,3,4],6
返回：4
'''
def getHeight(men, n):
        # write code here
        a=[0 for i in range(n)]
        a[0]=1
        for i in range(n):
            num=1
            for j in range(i):
                if men[i]>men[j]:
                    if a[j]+1>num:
                        num=a[j]+1
                        
            a[i]=num
            
        return max(a)