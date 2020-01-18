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
        if n == 0: return
        if n >= 1:
            u = [1]
            o = [0]
            none = [2]
        for i in range(2, n+1):
            print(i)
            u.append(u[i-2]*none[i-2]-o[i-2])
            o.append(i*(i-1)/2*u[i-2])
            none.append(i+1)
        print(u)
        print(o)
        print(none)
        return u[n-1]
s = Solution().numTrees(5)