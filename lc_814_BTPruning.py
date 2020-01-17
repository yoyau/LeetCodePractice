# -*- coding: utf-8 -*-
"""
814. Binary Tree Pruning
"""

from createBT import BTRoot

class Solution(object):
    
    def pruneTree(self, root):
        """
        much faster
        """
        if not root: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not (root.val or root.left or root.right):
            return None
        return root
    
    def pruneTree_1(self, root):
        """
        employ "isUniZero"
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
        return self.isUniZero(node.left) and self.isUniZero(node.right)

root = BTRoot([1,0,1,0,0,0,1]).get_root()
s = Solution()
s.pruneTree(root)