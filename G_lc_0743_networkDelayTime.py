# -*- coding: utf-8 -*-
"""
743. Network Delay Time -> Bellmand-Ford
"""

import collections
import heapq

class Solution(object):
    def networkDelayTime_BF(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # convert to outList
        outList = [[] for i in range(N)]
        for edge in times:
            outList[edge[0]-1].append((edge[1], edge[2]))

        # contruct dist list
        inf = 100*100
        dist = [inf for i in range(N)]
        dist[K-1] = 0
        for ite in range(N):
            change = False
            for node in range(N):
                for edge in outList[node]:
                    new = dist[node] + edge[1]
                    if new < dist[edge[0]-1]:
                        dist[edge[0]-1] = new
                        change = True
            if not change:
                break
        
        
        # check all reachable and maximum
        max_ = 0
        for i in dist:
            if i == inf:
                return -1
            else:
                if i > max_:
                    max_ = i
        return max_
    
    def networkDelayTime_DK(self, times, N, K):
        black = [False for i in range(N)]
        dist = []
        
            

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
output = Solution().networkDelayTime_BF(times, N, K)
