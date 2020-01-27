# -*- coding: utf-8 -*-
"""
104. Maximum Depth of Binary Tree
    
    level-order traversel, depth+=1 if new level is found

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth_0(self, root):
        """
        almost the same
        """
        if not root: return 0
        d = max(self.maxDepth_0(root.left), self.maxDepth_0(root.right)) + 1
        return d
        
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.q1=[root]
        self.q2=[]
        self.depth=0
        self.visit(self.q1, self.q2)
             
        return self.depth
        
    def visit(self, q1, q2):
        if q1 == []:
            return
        while q1 != []:
            if q1[0].left: q2.append(q1[0].left)
            if q1[0].right: q2.append(q1[0].right)
            del q1[0]
        self.depth+=1
        self.visit(q2, q1)