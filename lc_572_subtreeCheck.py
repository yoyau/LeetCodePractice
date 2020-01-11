# -*- coding: utf-8 -*-
"""
572. Subtree of Another Tree
"""

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t: return True
        if not s and t: return False
        if not t and s: return True
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right.t)
    
    def isSameTree(self, p, q):
        if not p and not q: return True
        if (not p and q) or (not q and p): return False
        
        if p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        else:
            return False