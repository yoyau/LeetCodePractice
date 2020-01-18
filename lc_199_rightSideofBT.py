# -*- coding: utf-8 -*-
"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
"""

class Solution:
    def rightSideView(self, root):
        if not root: return []
        self.q1=[root]
        self.q2=[]
        self.l=[]
        self.visit(self.q1, self.q2)
             
        return [l[-1] for l in self.l]
        
    def visit(self, q1, q2):
        if q1 == []:
            return
        temp = []
        while q1 != []:
            temp.append(q1[0].val)
            if q1[0].left: q2.append(q1[0].left)
            if q1[0].right: q2.append(q1[0].right)
            del q1[0]
        self.l.append(temp)
        self.visit(q2, q1)