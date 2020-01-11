# -*- coding: utf-8 -*-
"""
589. N-ary Tree Preorder Traversal
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.l=[]
        if not root:
            return []
        self.visit(root)
        return self.l
    
    def visit(self, root):
        if not root.val:
            return
        self.l += [root.val]
        for chi in root.children:
            self.visit(chi)
        
