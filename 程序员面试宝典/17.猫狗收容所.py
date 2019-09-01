# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:09:06 2019

@author: Tang
"""

'''
题目描述



       有家动物收容所只收留猫和狗，但有特殊的收养规则，收养人有两种收养方式，
       第一种为直接收养所有动物中最早进入收容所的，第二种为选择收养的动物类型（猫或狗），
       并收养该种动物中最早进入收容所的。 

       给定一个操作序列int[][2] ope(C++中为vector<vector<int>>)代表所有事件。
       若第一个元素为1，则代表有动物进入收容所，第二个元素为动物的编号，正数代表狗，
       负数代表猫；若第一个元素为2，则代表有人收养动物，第二个元素若为0，
       采取第一种收养方式，若为1，则指定收养狗，若为-1则指定收养猫。请按顺序返回收养的序列。
       若出现不合法的操作，即没有可以符合领养要求的动物，则将这次领养操作忽略。 

测试样例： 
[[1,1],[1,-1],[2,0],[2,-1]]
返回：[1,-1]
'''
def asylum(self, ope):
        # write code here
        dog,cat,all_list,res=[],[],[],[]
        for i in ope:
            if i[0]==1:
                if i[1]>0:
                    dog.append(i[1])
                    all_list.append(i[1])
                else:
                    cat.append(i[1])
                    all_list.append(i[1])
            elif i[0]==2:
                if i[1]==0:
                    if all_list:
                        tmp=all_list.pop(0)
                        if tmp>0:
                            dog.pop(0)
                        else:
                            cat.pop(0)
                        #all_list.remove(tmp)
                        res.append(tmp)
                elif i[1]==1:
                    if len(dog)>0:
                        tmp=dog.pop(0)
                        res.append(tmp)
                        all_list.remove(tmp)
                elif i[1]==-1:
                    if len(cat)>0:
                        tmp=cat.pop(0)
                        res.append(tmp)
                        all_list.remove(tmp)
                else:
                    continue
        return res
a=[1,2,3,4]
tmp=a.pop(0)
print(a)