# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:25:33 2019

@author: Tang
"""

class Solution:
    def solve(self, n):
        nums = [1, 5, 10, 20, 50, 100]  # 基本面额
        dp = [1] * (n + 1)  # 初始化dp

        for j in range(1, 3):
            for i in range(1, n+1):
                if i >= nums[j]:  # 约束条件
                    dp[i] += dp[n - nums[j]]
                    print(dp)
        return dp[-1]


if __name__ == '__main__':
    solu = Solution()
    print(solu.solve(n=10))
