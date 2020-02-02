# -*- coding: utf-8 -*-
"""
Given a binary tree, return the inorder traversal of its nodes' values.
"""

from createBT import BTRoot

class Solution:
    def inorderTraversal_0(self, root):
        if not root: return []
        return self.inorderTraversal_0(root.left) + [root.val] + self.inorderTraversal_0(root.right)
    
    def inorderTraversal(self, root):
        self.val = []
        self.visit(root)
        return self.val
    
    def visit(self, node):
        if not node: return
        self.visit(node.left)
        self.val.append(node.val)
        self.visit(node.right)
            

root = BTRoot([1, None, 2, None, None, 3]).get_root()
val = Solution().inorderTraversal_0(root)