# -*- coding: utf-8 -*-
"""
310. Minimum Height Trees
"""

import time

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adjList = [[] for i in range(n)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        to_be_deleted = [ind for ind, length in enumerate(adjList) if len(length) == 1]
        to_be_deleted_2 = []
             
        while to_be_deleted:

            if len(to_be_deleted) == 2 and adjList[to_be_deleted[0]][0] == to_be_deleted[1] and adjList[to_be_deleted[1]][0] == to_be_deleted[0]:
                return to_be_deleted
            i = to_be_deleted[0]
            
            for neighbor in adjList[i]:
                print(adjList)
                print(to_be_deleted)
                print(to_be_deleted_2)
                adjList[neighbor].remove(i)
                del adjList[i][0]
                
                if len(adjList[neighbor]) == 0:
                    return [neighbor]
                elif len(adjList[neighbor]) == 1:
                    to_be_deleted_2.append(neighbor)
            del to_be_deleted[0]
            to_be_deleted, to_be_deleted_2 = to_be_deleted_2, to_be_deleted
        
n = 4
edges = [[1, 0], [1, 2], [1, 3]]

#n = 6
#edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

t_s = time.time()
r = Solution().findMinHeightTrees(n, edges)
t = time.time()-t_s