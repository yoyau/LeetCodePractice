# -*- coding: utf-8 -*-
"""
207. Course Schedule -> check if G is a DAG (topological sort)
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Convert edge to incoming adjacency linked list
        indeg = [0 for i in range(numCourses)]
        outList = [[] for i in range(numCourses)]
        for edge in prerequisites:
            outList[edge[0]].append(edge[1])
            indeg[edge[1]] += 1
        
        # delete one node with indeg == 0 
        ts = 0
        to_be_deleted = [i for i, deg in enumerate(indeg) if deg == 0]
        if not to_be_deleted: return False
        
        while to_be_deleted:
            print(to_be_deleted)
            i = to_be_deleted.pop()
            ts += 1
            for neighbor in outList[i]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    to_be_deleted.append(neighbor)
        print(ts)
        if ts <= numCourses: 
            return True
        else:
            return False
        
num = 3
pre = [[0,2],[1,2]]
result = Solution().canFinish(num, pre)