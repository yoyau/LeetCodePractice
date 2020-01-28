# -*- coding: utf-8 -*-
"""
399. Evaluate Division
"""

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # convert edges to outList
        equations += [[i, j] for j, i in equations]
        values += [1/v for v in values]
        self._outList = dict()
        for i, eqa in enumerate(equations):
            if eqa[0] in self._outList:
                self._outList[eqa[0]][eqa[1]] = values[i]
            else:
                self._outList[eqa[0]] = {eqa[1]:values[i]}
        
        ans = []
        for q in queries:
            if q[0] in self._outList:
                ans.append(self.divide(q[0], q[1], []))
            else:
                ans.append(-1)
        return ans
    
    def divide(self, i, j, visited):
        if i==j: return 1
        # visited is used to avoid re-visit parents (deadlock)
        visited.append(i)
        
        # dfs 
        for neighbor in self._outList[i]:
            if neighbor not in visited:   
                m = self.divide(neighbor, j, visited)
                
                # if m == -1 represents its neighbor couldn't reach target
                if m > 0:
                    return m * self._outList[i][neighbor]
        else:
            return -1
            
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
r = Solution().calcEquation(equations, values, queries)