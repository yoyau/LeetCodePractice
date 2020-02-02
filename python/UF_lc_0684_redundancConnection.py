# -*- coding: utf-8 -*-
"""
684. Redundant Connection
"""

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        V_num = len(edges)
        self._parent = list(range(V_num+1))
        self._rank = [0] * (V_num+1)
        for edge in edges:
            rc = self.merge(edge[0], edge[1])
            if rc:
                return rc
            
        print(self._parent)
        print(self._rank)
        
    def find(self, x):
        if x != self._parent[x]:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def merge(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_y == p_x:
            return [x,y]
        if self._rank[p_x] == self._rank[p_y]:
            self._rank[p_x] += 1
            self._parent[p_y] = p_x
        elif self._rank[p_x] > self._rank[p_y]:
            self._parent[p_y] = p_x
        else:
            self._parent[p_x] = p_y
            
input_ = [[1,2], [2,3], [3,4], [1,4], [1,5]]
output = Solution().findRedundantConnection(input_)