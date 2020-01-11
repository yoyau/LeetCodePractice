# -*- coding: utf-8 -*-
"""
538. Convert BST to Greater Tree

hint: in-order visit inversely
"""

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.nodes = []
        self.visit(root)
        return root
        
    def visit(self, root):
        
        if root.right:
            self.visit(root.right)
        
        if root.left:
            self.nodes.append(root)
            if len(self.nodes) >= 2 :
                root.val += self.nodes[-2].val 
            self.visit(root.left)    
        else:
            self.nodes.append(root)
            if len(self.nodes) >= 2 :
                root.val += self.nodes[-2].val 
