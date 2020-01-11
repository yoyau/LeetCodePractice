# -*- coding: utf-8 -*-
"""
993. Cousins in Binary Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):        
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root: return
        self.q1=[root]
        self.q2=[]
        level_vals = [root.val]

        while level_vals != []:
            if x in level_vals and y in level_vals: return True
            if x in level_vals or y in level_vals: return False
            level_vals = self.visit(self.q1, self.q2, x, y)    
            self.q1, self.q2 = self.q2, self.q1
        return False
    
    def visit(self, q1, q2, x, y):
        if q1 == []:
            return []
        temp = []
        while q1 != []:
            temp.append(q1[0].val)
            if (q1[0].left and q1[0].right):
                if (q1[0].left.val == x and q1[0].right.val == y) or (q1[0].left.val == y and q1[0].right.val == x):
                    temp = []
                    return
                else:
                    q2.append(q1[0].left)
                    q2.append(q1[0].right)
            if q1[0].left: q2.append(q1[0].left)
            if q1[0].right: q2.append(q1[0].right)
            del q1[0]
        return temp