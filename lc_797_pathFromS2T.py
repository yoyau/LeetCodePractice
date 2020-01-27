# -*- coding: utf-8 -*-
"""
797. All Paths From Source to Target
"""

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # graph is already in the "outList" form
        return self.path(0, graph)

    def path(self, start, graph):
        ps = []
        for neighbor in graph[start]:
            p = [start]
            if not graph[neighbor]:
                p.append(neighbor)
                ps.append(p)
            else:
                future_path = self.path(neighbor, graph)
                for fp in future_path:
                    ps.append(p+fp)
        return ps

     
        
input_ = [[1,2], [3], [], []] 
o = Solution().allPathsSourceTarget(input_)