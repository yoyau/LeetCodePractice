# -*- coding: utf-8 -*-
"""
310. Minimum Height Trees
"""

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 2:
            return edges
        
        root = list(range(n))
        count = [0]*n
        for edge in edges:
            for v in edge:
                count[v]+=1
        root = [i for i in root if i not in [i for i, c in enumerate(count) if c==1]]
        edges = [edge for edge in edges if (edge[0] in root and edge[1] in root)]
        print(edges)
        return self.findMinHeightTrees(len(root), edges)
        

n = 4
edges = [[1,0],[1,2],[1,3]]
r = Solution().findMinHeightTrees(n, edges)