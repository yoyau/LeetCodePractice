# -*- coding: utf-8 -*-
"""
96. Unique Binary Search Trees

#n: # of unique way to distribute nodes

#0 = 1

#1 = #0 * #0

#2 = #1 * #0
   + #0 * #1

#3 = #2 * #0
   + #1 * #1
   + #0 * #2
     .
     .
     .
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