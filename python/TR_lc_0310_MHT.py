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
        # map edges to adajacency List
        adjList = [[] for i in range(n)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        to_be_deleted = [ind for ind, length in enumerate(adjList) if len(length) == 1]
        to_be_deleted_2 = []
             
        while True:
            print(to_be_deleted)
            print(adjList)
            if len(to_be_deleted) == 2 and adjList[to_be_deleted[0]][0] == to_be_deleted[1] and adjList[to_be_deleted[1]][0] == to_be_deleted[0]:
                return to_be_deleted
            for i in to_be_deleted:
                for neighbor in adjList[i]:
                    adjList[neighbor].remove(i)
                    if len(adjList[neighbor]) == 0:
                        return [neighbor]
                    elif len(adjList[neighbor]) == 1:
                        to_be_deleted_2.append(neighbor)         
            to_be_deleted, to_be_deleted_2 = to_be_deleted_2, []
        

n = 7
edges = [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]


t_s = time.time()
r = Solution().findMinHeightTrees(n, edges)
t = time.time()-t_s