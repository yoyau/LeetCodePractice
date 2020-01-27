# -*- coding: utf-8 -*-
"""
965. Univalued Binary Tree

1) visiting all nodes in "pre-order"

"""

from TreeNode import TreeNode


class Solution1(object):
    def isUnivalTree(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.unival = root.val
        self.uni = True
        self.visit(root)
        return self.uni
    
    def visit(self, root, uni=True):
        # check uni
        if root.val != self.unival:
            self.uni = False
        
        # check left
        if root.left != None:
            self.visit(root.left)
        
        # check right
        if root.right != None:
            self.visit(root.right)
            

class Solution2(object):
    def isUnivalTree(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: bool
        """   
        return self.isUniNode(root, root.val)
    
    def isUniNode(self, node, unival):
        if not node: return True
        if node.val != unival:
            return False
        return self.isUniNode(node.left, unival) and self.isUniNode(node.right, unival)
        
        
