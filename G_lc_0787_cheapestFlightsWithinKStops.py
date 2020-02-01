# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:24:42 2020

@author: yoyau
"""
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        # contruct dist list
        inf = int(1e6+1)
        dist = [inf for i in range(n)]
        dist[src] = 0
        for ite in range(K+1):      
            change = False
            new_dist = dist[:]
            for flight in flights:
                new = dist[flight[0]] + flight[2]
                if new < new_dist[flight[1]]:
                    new_dist[flight[1]] = new
                    change = True
            dist = new_dist
            if not change:
                break
        if dist[dst] == inf:
            return -1
        else:
            return dist[dst]
        

n = 5
edges=[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
src = 0
dst = 2
k = 2
r = Solution().findCheapestPrice(n, edges, src, dst, k)