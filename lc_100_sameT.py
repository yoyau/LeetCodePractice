# -*- coding: utf-8 -*-
"""
100. Same Tree
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

p = TreeNode(1)
p.left = TreeNode(2)
q = TreeNode(1)
q.right = TreeNode(2)        


class Solution(object):
    
    def isSameTree_0(self, p, q):
        """
        If we dont care the real val in tree, then this method is much more faster.
        """
        if not p and not q:
            return True
        
        if (not p and q) or (not q and p): return False
        
        if p.val == q.val:
            return (self.isSameTree_0(p.left, q.left) and self.isSameTree_0(p.right, q.right))
        else:
            return False  
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True
        if (not p and q) or (not q and p): return False
        self.p_q1=[p]
        self.p_q2=[]
        self.q_q1=[q]
        self.q_q2=[]
        same = self.visit(self.p_q1, self.p_q2, self.q_q1, self.q_q2)
        return same
        
    def visit(self, p_q1, p_q2, q_q1, q_q2):
        p_level_vals = [p_q1[0].val]
        q_level_vals = [q_q1[0].val]

        while p_level_vals == q_level_vals:
            print(p_q1, p_q2)
            if p_level_vals == []: return True
            p_level_vals = self.level_visit(p_q1, p_q2)
            q_level_vals = self.level_visit(q_q1, q_q2)
            p_q1, p_q2 = p_q2, p_q1
            q_q1, q_q2 = q_q2, q_q1
        return False
      
    def level_visit(self, q1, q2):        
        if q1 == []:
            return []
        level_vals = []
        while q1 != []:
            if q1[0]:
                level_vals.append(q1[0].val)
                if q1[0].left:
                    q2.append(q1[0].left)
                else:
                    q2.append(None)
                if q1[0].right:
                    q2.append(q1[0].right)
                else:
                    q2.append(None)
            else:
                level_vals.append(None)
            del q1[0]
        return level_vals

s = Solution()
#same = s.isSameTree(p, q)
same = s.isSameTree_0(p, q)