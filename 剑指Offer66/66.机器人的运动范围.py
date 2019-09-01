# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:48:04 2019

@author: Tang
"""

'''
题目描述


地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四
个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，
机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），
因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''
a=[[1 for i in range(3)] for i  in range(4)]
print(a)

def movingCount(threshold, rows, cols):
        # write code here
        
        #a=[[1 for i in range(cols)] for j  in range(rows)]
        dic=dict()
        def digui(i,j):
            
            
            #s = sum(map(int,str(i)+str(j)))
            if (i,j) in dic:
                return 0
            #s=i/10 + i%10 +j/10 +j%10
            if i<rows and i>=0 and j<cols and j>=0:
                
                if sum(list(map(int,str(i)+str(j))))<=threshold :
                    #count+=1
                    #a[i][j]=0
                    dic[(i,j)]=1
                    return 1+digui(i+1,j) + digui(i-1,j) + digui(i,j-1) + digui(i,j+1)
                else:
                    #a[i][j]=2
                    return 0
            else:
                return 0
        
        return digui(0,0)
print(movingCount(18,20,20))