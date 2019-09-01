# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:08:10 2019

@author: Tang
"""
m,n=5,5
res=[[1000 for i in range(m+1)] for j in range(n+1)]
res[0][0]=0
print(res[-1][0])
'''
题目描述



在一个nxm矩阵形状的城市里爆发了洪水，洪水从(0,0)的格子流到这个城市，在这个矩阵中有的格子有一些建筑，
洪水只能在没有建筑的格子流动。请返回洪水流到(n - 1,m - 1)的最早时间(洪水只能从一个格子流到其相邻的
格子且洪水单位时间能从一个格子流到相邻格子)。 

给定一个矩阵map表示城市，其中map[i][j]表示坐标为(i,j)的格子，值为1代表该格子有建筑，0代表没有建筑。
同时给定矩阵的大小n和m(n和m均小于等于100)，请返回流到(n - 1,m - 1)的最早时间。保证洪水一定能流到终点。 
'''
def floodFill(tmap, n, m): #方法1
        # write code here
        res=[[1000 for i in range(m+1)] for j in range(n+1)]
        res[0][0]=0
        for i in range(n):
            for j in range(m):
                if i==0 and j==0 :
                    continue
                if tmap[i][j]==0:
                    res[i][j]=min(res[i-1][j],res[i+1][j],res[i][j-1],res[i][j+1])+1
        return res[n-1][m-1]
def floodFill( tmap, n, m): #方法2
        visited = [[False for i in range(m)] for j in range(n)]
        # print(visited)
        self.ans = float('inf')
        print(self.ans)
 
        def dfs(row, col, visited, step):
            if row<0 or row>=n or col<0 or col>=m or tmap[row][col] or visited[row][col]:
                return None
            if row==n-1 and col==m-1:
                self.ans = min(self.ans, step)
                return
            visited[row][col] = True
 
             # 很重要 顺序不能变
            dfs(row + 1, col, visited, step + 1)
            dfs(row, col + 1, visited, step + 1)
            dfs(row, col - 1, visited, step + 1)
            dfs(row - 1, col, visited, step + 1)
 
        dfs(0, 0, visited, 0)
 
        return self.ans
