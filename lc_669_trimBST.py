# -*- coding: utf-8 -*-
"""
669. Trim a Binary Search Tree
"""

from createBT import BTRoot

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root: return
        
        if root.val < L:  
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
            
root = BTRoot([1, 0, 2]).get_root()
root_trimmed = Solution().trimBST(root, 1, 2)