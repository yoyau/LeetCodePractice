# -*- coding: utf-8 -*-
"""
226. Invert Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return 
        root.right, root.left = root.left, root.right
        if root.left: self.invertTree(root.left)
        if root.right: self.invertTree(root.right)
        return root