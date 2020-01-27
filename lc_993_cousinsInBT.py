# -*- coding: utf-8 -*-
"""
993. Cousins in Binary Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):        
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.q1=[root]
        self.q2=[]   
        self.level_ind = [1]        
        return self.visit(self.q1, self.q2, x, y)
    
    def visit(self, q1, q2, x, y):
        if q1 == []:
            return False
        
        target_ind = []
        while q1 != []:
            node = q1.pop(0)
            node_ind = self.level_ind.pop(0)
            if node.val == x or node.val == y:
                target_ind.append(node_ind)
            if node.left: 
                q2.append(node.left)
                self.level_ind.append(2*node_ind)
            if node.right: 
                q2.append(node.right)
                self.level_ind.append(2*node_ind+1)
        
        if len(target_ind) == 1: return False
        if len(target_ind) == 2 and abs(target_ind[0]//2 != target_ind[1]//2):
            return True
        else:
            return self.visit(q2, q1, x, y)