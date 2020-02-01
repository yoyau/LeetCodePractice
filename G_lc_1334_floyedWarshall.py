# -*- coding: utf-8 -*-
"""
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
"""

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        inf = int(1e6)+1
        M = [[ inf for i in range(n)] for j in range(n)]
        for f, t, w in edges:
                M[f][t] = w
                M[t][f] = w
        for i in range(n):
            M[i][i] = 0
        for mid in range(n):
            for f in range(n):
                for t in range(n):
                    M[f][t] = min(M[f][t], M[f][mid]+M[mid][t])
                    M[t][f] = M[f][t]

        
        minimum = inf
        ind = -1
        for new_ind, endCity in enumerate(M):
            new_minimum = len([1 for i in endCity if i <= distanceThreshold])
            if new_minimum <= minimum:
                minimum = new_minimum
                ind = new_ind
        return ind
#n = 5
#edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
#distanceThreshold = 2
n = 6
edges =[[2,3,7],[2,5,8],[0,2,8],[4,5,5],[1,5,10],[3,4,3],[0,5,9],[1,2,1]]
distanceThreshold = 3269
output = Solution().findTheCity(n, edges, distanceThreshold)