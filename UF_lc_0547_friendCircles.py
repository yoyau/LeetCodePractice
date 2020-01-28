# -*- coding: utf-8 -*-
"""
547. Friend Circles
"""

class Solution_0:
    def findCircleNum(self, M: [[int]]) -> int:
        num = len(M)
        
        # Solve by Union find
        self.friend = list(range(num))
        self.rank = [0]*num
        for i in range(1, num):
            for j in range(i):
                if M[i][j]:
                    self.merge(i, j)
        
        for i in range(num):
            self.find(i)
        print(self.friend)
        return len([1 for i, val in enumerate(self.friend) if self.friend[i]==i])
    
    def find(self, x):
        if x != self.friend[x]:
            self.friend[x] = self.find(self.friend[x])
        return self.friend[x]
    
    def merge(self, x, y):
        bf_x = self.find(x)
        bf_y = self.find(y)
        if bf_x == bf_y: return
        if self.rank[bf_x] == self.rank[bf_y]:
            self.rank[bf_x] += 1
            self.friend[bf_y] = bf_x
        elif self.rank[bf_x] > self.rank[bf_y]:
            self.friend[bf_y] = bf_x
        else:
            self.friend[bf_x] = bf_y


input_=[[1,1,1],[1,1,1],[1,1,1]]
cycle = Solution_0().findCircleNum(input_)
