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
            ans.append(self.divide(queries[0], queries[1]))
        return ans
    
    def divide(self, i, j):
        if self._outList[i][j]:
            return self._outList[i][j]
        else:
            for neighbor in self._outList[i]:
                self.divide(neighbor, j)

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
r = Solution().calcEquation(equations, values, queries)