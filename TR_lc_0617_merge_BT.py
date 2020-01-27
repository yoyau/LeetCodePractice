# -*- coding: utf-8 -*-
"""
617. Merge Two Binary Trees
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1: return t2
        if not t2: return
        
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        
        return t1

t_1 = TreeNode(3)
t_1.left = TreeNode(5)

t_2 = TreeNode(1)
t_2.right = TreeNode(4)

def testFun(t1, t2):
    t1, t2 = t2, t1

testFun(t_1, t_2)


    
    