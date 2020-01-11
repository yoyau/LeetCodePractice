# -*- coding: utf-8 -*-
"""
110. Balanced Binary Tree
"""

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return (abs(self.maxDepth(root.left)-self.maxDepth(root.right)) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def maxDepth(self, root):
        if not root: return 0
        d = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return d
