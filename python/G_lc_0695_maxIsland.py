# -*- coding: utf-8 -*-
"""
695. Max Area of Island
"""

class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        if not grid: return 0
        islandsNum = []
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == 1:
                    islandsNum.append(self.dfs(i, j))

        if not islandsNum: 
            return 0
        else:
            return max(islandsNum)            
        
    def dfs(self, i , j):
        # check boundary
        if i < 0 or i == self.height: return 0
        if j < 0 or j == self.width: return 0
        
        # check isLand and prohibit "go back"
        if self.grid[i][j] == "F" or self.grid[i][j] == 0: return 0
        self.grid[i][j] = "F"
        
        # dfs 4-direction
        return 1 + self.dfs(i+1, j) + self.dfs(i, j+1) + self.dfs(i-1, j) + self.dfs(i, j-1)
        
        
        
#grid = [[0]]
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
area = Solution().maxAreaOfIsland(grid)