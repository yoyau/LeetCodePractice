# -*- coding: utf-8 -*-
"""
802. Find Eventual Safe States
"""

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # Convert edge to incoming adjacency linked list
        numNode = len(graph)
        outdeg = [0 for i in range(numNode)]
        inList = [[] for i in range(numNode)]
        for i, outEdge in enumerate(graph):
            outdeg[i] += len(outEdge)
            for node in outEdge:
                inList[node].append(i)    
        print(inList)
        print(outdeg)
        
        # delete one node with outdeg == 0 
        safeStates = []
        to_be_deleted = [i for i, deg in enumerate(outdeg) if deg == 0]
        if not to_be_deleted: return []
        
        while to_be_deleted:
#            print(to_be_deleted)
            i = to_be_deleted.pop()
            safeStates.append(i)
            for preState in inList[i]:
                outdeg[preState] -= 1
                if outdeg[preState] == 0:
                    to_be_deleted.append(preState)

        return sorted(safeStates)

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
output = Solution().eventualSafeNodes(graph)