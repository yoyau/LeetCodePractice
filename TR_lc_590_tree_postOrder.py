# -*- coding: utf-8 -*-
"""
590. N-ary Tree Postorder Traversal
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    l = []
    def postorder(self, root):
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
        if root.val == None:
            return
        for chi in root.children:
            self.visit(chi)
        self.l += [root.val]