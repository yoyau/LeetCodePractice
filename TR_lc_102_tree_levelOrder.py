# -*- coding: utf-8 -*-
"""
102. Binary Tree Level Order Traversal

    use two queue alternately to record each level nodes
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        self.q1=[root]
        self.q2=[]
        self.l=[]
        self.visit(self.q1, self.q2)
             
        return self.l
        
    def visit(self, q1, q2):
        if q1 == []:
            return
        temp = []
        while q1 != []:
            temp.append(q1[0].val)
            if q1[0].left: q2.append(q1[0].left)
            if q1[0].right: q2.append(q1[0].right)
            del q1[0]
        self.l.append(temp)
        self.visit(q2, q1)