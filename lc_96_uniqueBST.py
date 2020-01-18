# -*- coding: utf-8 -*-
"""
96. Unique Binary Search Trees

"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]
        for i in range(n):
            unique=0
            for j in range(i+1):
                unique+=dp[j]*dp[i-j]
            dp.append(unique)
        return dp[n]
s = Solution().numTrees(5)