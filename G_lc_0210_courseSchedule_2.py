# -*- coding: utf-8 -*-
"""
210. Course Schedule II
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Convert edge to incoming adjacency linked list
        indeg = [0 for i in range(numCourses)]
        outList = [[] for i in range(numCourses)]
        for edge in prerequisites:
            outList[edge[1]].append(edge[0])
            indeg[edge[0]] += 1
        
        # delete one node with indeg == 0 
        course = []
        to_be_deleted = [i for i, deg in enumerate(indeg) if deg == 0]
        if not to_be_deleted: return []
        
        while to_be_deleted:
            i = to_be_deleted.pop()
            course.append(i)
            for neighbor in outList[i]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    to_be_deleted.append(neighbor)
        if len(course) == numCourses: 
            return course
        else:
            return []
        
num = 4
pre = [[1,0],[2,0],[3,1],[3,2]]
result = Solution().findOrder(num, pre)