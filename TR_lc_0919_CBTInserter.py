# -*- coding: utf-8 -*-
"""
919. Complete Binary Tree Inserter
"""

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        self.q1=[self.root]
        self.q2=[]
        return self.visit(self.q1, self.q2, v)
        
    
    def visit(self, q1, q2, v):
        if q1 == []:
            return

        while q1 != []:

            if q1[0].left and q1[0].right:
                q2.append(q1[0].left)
                q2.append(q1[0].right)
            elif q1[0].left:
                q1[0].right = TreeNode(v)
                return q1[0].val
            else:
                q1[0].left = TreeNode(v)
                return q1[0].val           
            
            del q1[0]
            
        return self.visit(q2, q1, v)
        
    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
        

