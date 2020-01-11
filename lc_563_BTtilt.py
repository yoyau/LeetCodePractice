# -*- coding: utf-8 -*-
"""
563. Binary Tree Tilt
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.total_t = 0
        self.visit(root)
        return self.total_t
    
    def visit(self, root):
        if not root: return
        self.total_t+=self.nodesTilt(root)
        if root.left:
            self.visit(root.left)
        if root.right:
            self.visit(root.right)
    
    def nodesTilt(self, node):   
        if not node: return 0   
        if node.left and node.right:
            t = abs(self.nodesValSum(node.left) - self.nodesValSum(node.right))
        elif node.left and not node.right:
            t = self.nodesValSum(node.left)
        elif node.right and not node.left:
            t = self.nodesValSum(node.right)
        else:
            return 0
        return t
        
    def nodesValSum(self, node):
        if not node: return 0
        s = 0
        if node.left:
            s+=self.nodesValSum(node.left)
        if node.right:
            s+=self.nodesValSum(node.right)
        return s+node.val
