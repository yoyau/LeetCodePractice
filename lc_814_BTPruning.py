# -*- coding: utf-8 -*-
"""
814. Binary Tree Pruning
"""

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        if self.isUniZero(root): 
            return
        if self.isUniZero(root.left): root.left = None
        if self.isUniZero(root.right): root.right = None
        self.pruneTree(root.left)
        self.pruneTree(root.right)
        return root

    def isUniZero(self, node):
        if not node: return True
        if node.val != 0:
            return False
        return self.isUniNode(node.left) and self.isUniNode(node.right)