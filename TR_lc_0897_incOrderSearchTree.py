# -*- coding: utf-8 -*-
"""
897. Increasing Order Search Tree
    
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.nodes = []
        self.visit(root)
        
        for i, node in enumerate(self.nodes):
            node.left = None
            if i < len(self.nodes-1):
                node.right = self.nodes[i+1]
        return self.nodes[0]
        
    def visit(self, root):
        
        if root.left:
            self.visit(root.left)
        
        if root.right:
            self.nodes.append(root)
            self.visit(root.right)    
        else:
            self.nodes.append(root)