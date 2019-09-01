# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:32:50 2019

@author: Tang
"""

'''
题目描述



对于一个给定的井字棋棋盘，请设计一个高效算法判断当前玩家是否获胜。

给定一个二维数组board，代表当前棋盘，其中元素为1的代表是当前玩家的棋子，为0表示没有棋子，为-1代表是对方玩家的棋子。

测试样例：
[[1,0,1],[1,-1,-1],[1,-1,0]]
返回：true
'''
def checkWon( board):
        # write code here
        n=len(board)
        s1=0
        s2=0
        for i in range(n):
            if board[i][0]==1 and board[i][1]==1 and board[i][2]==1: #行==1
                return True
            if board[0][i]==1 and board[1][i]==1 and board[2][i]==1:#列==1
                return True
            if board[i][i]==1:#正对角线
                s1+=1
            if board[n-i-1][i]==1:#逆对角线
                s2+=1
        if s1==n or s2==n:
            return True
        return False
   
import time 

def get_time(func):
    startTime = time.time()
    func()
    endTime = time.time()
    processTime = (endTime - startTime) * 1000
    print ("The function timing is %f ms" %processTime)

def myfunc():
    print( "start func")
    time.sleep(0.8)
    print ("end func")

get_time(myfunc)
myfunc()     
     

     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     