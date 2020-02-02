# -*- coding: utf-8 -*-
"""
733. Flood Fill
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image: return
        self.grid = image
        self._height = len(self.grid)
        self._width = len(self.grid[0])
        self._newColor = newColor
        self._oldColor = self.grid[sr][sc]
        
        self.dfs(sr, sc)
        return self.grid        
        
    def dfs(self, i , j):
        # check boundary
        if i < 0 or i == self._height: return
        if j < 0 or j == self._width: return
        
        # check isLand and prohibit "go back"
        if self.grid[i][j] == self._newColor or self.grid[i][j] != self._oldColor: return
        self.grid[i][j] = self._newColor
        
        # dfs 4-direction
        self.dfs(i+1, j)
        self.dfs(i, j+1)
        self.dfs(i-1, j)
        self.dfs(i, j-1)
        
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
o = Solution().floodFill(image, sr, sc, newColor)