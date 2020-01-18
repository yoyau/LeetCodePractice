# -*- coding: utf-8 -*-
"""
222. Count Complete Tree Nodes
"""
from createBT import BTRoot


class Solution:
    def countNodes(self, root) -> int:
        if not root: return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
             


root = BTRoot([1,2,3,4,5,6,None]).get_root()
s = Solution()
steps = s.countNodes(root)