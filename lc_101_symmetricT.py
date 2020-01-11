# -*- coding: utf-8 -*-
"""
101. Symmetric Tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

p = TreeNode(1)
p.left = TreeNode(2)
q = TreeNode(1)
q.right = TreeNode(2)  
root = TreeNode(0)
root.left = p
root.right = q

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        sym = self.isSym(root.left, root.right)
        return sym
    
    def isSym(self, p, q):
        
        if not p and not q:
            return True
        
        if (not p and q) or (not q and p): return False
        
        if p.val == q.val:
            return (self.isSym(p.left, q.right) and self.isSym(p.right, q.left))
        else:
            return False  
        
s = Solution()
same = s.isSymmetric(root)      