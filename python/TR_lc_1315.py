# -*- coding: utf-8 -*-
"""
1315. Sum of Nodes with Even-Valued Grandparent
"""
from createBT import BTRoot

class Solution:
    def sumEvenGrandparent(self, root) -> int:
        self.q1=[root]
        self.q2=[]
        self.even_gp={0:False}
        self.ind = [1]
        self.gc=[]
        self.visit(self.q1, self.q2)
        print(self.gc)
        return sum(self.gc)
        
    def visit(self, q1, q2):
        if q1 == []:
            return
        while q1 != []:
            if self.even_gp[(self.ind[0]//2)//2]:
                self.gc.append(q1[0].val)
                
            if q1[0].val % 2 == 0:
                self.even_gp[self.ind[0]] = True
            else:
                self.even_gp[self.ind[0]] = False
                
            if q1[0].left: 
                q2.append(q1[0].left)
                self.ind.append(self.ind[0]*2)
            if q1[0].right: 
                q2.append(q1[0].right)
                self.ind.append(self.ind[0]*2+1)
                
            del q1[0]
            del self.ind[0]
        self.visit(q2, q1)
        
root = BTRoot([6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]).get_root()
s = Solution().sumEvenGrandparent(root)