# -*- coding: utf-8 -*-
"""
200. Number of Islands
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """ 
        if not grid: return 0
        islandsNum = 0
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == "1":
                    islandsNum+=1
                    self.dfs(i, j)
        return islandsNum            
        
    def dfs(self, i , j):
        # check boundary
        if i < 0 or i == self.height: return
        if j < 0 or j == self.width: return
        
        # check isLand and prohibit "go back"
        if self.grid[i][j] == "F" or self.grid[i][j] == "0": return
        self.grid[i][j] = "F"
        
        # dfs 4-direction
        self.dfs(i+1, j)
        self.dfs(i, j+1)
        self.dfs(i-1, j)
        self.dfs(i, j-1)

input_ = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
r = Solution().numIslands(input_)