# -*- coding: utf-8 -*-
"""
990. Satisfiability of Equality Equations
"""

class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        self._parent = list(range(26))
        self._rank = [0]*26
        equaEquations=[equ for equ in equations if equ[1] == '=']
        notEquations=[equ for equ in equations if equ[1] == '!']
        
        l = []
        for eqa in equaEquations:
            self.merge(ord(eqa[0])-ord('a'), ord(eqa[-1])-ord('a'))
            l.append(ord(eqa[0])-ord('a'))
            l.append(ord(eqa[-1])-ord('a'))
        
        for i in list(set(l)):
            if self._parent[i] != i:
                self.find(i)
        
        for eqa in notEquations:
            if not self.check(ord(eqa[0])-ord('a'), ord(eqa[-1])-ord('a')):
                return False
        return True
        
    def check(self, x, y):
        if self._parent[x] == self._parent[y]: 
            return False
        else:
            return True
        
    def find(self, x):
        if x != self._parent[x]:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def merge(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_y == p_x:
            return [x,y]
        if self._rank[p_x] == self._rank[p_y]:
            self._rank[p_x] += 1
            self._parent[p_y] = p_x
        elif self._rank[p_x] > self._rank[p_y]:
            self._parent[p_y] = p_x
        else:
            self._parent[p_x] = p_y
input_ =["a==b","c==d","a==c","a!=d"]
o = Solution().equationsPossible(input_)