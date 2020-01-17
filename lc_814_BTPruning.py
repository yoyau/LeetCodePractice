# -*- coding: utf-8 -*-
"""
814. Binary Tree Pruning
"""

from 

class Solution(object):
    
    def pruneTree(self, root):
    
    def pruneTree_1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        if self.isUniZero(root): 
            return
        if self.isUniZero(root.left): root.left = None
        if self.isUniZero(root.right): root.right = None
        self.pruneTree_1(root.left)
        self.pruneTree_1(root.right)
        return root

    def isUniZero(self, node):
        if not node: return True
        if node.val != 0:
            return False
        return self.isUniNode(node.left) and self.isUniNode(node.right)

