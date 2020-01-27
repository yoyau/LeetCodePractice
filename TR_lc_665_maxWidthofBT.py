# -*- coding: utf-8 -*-
"""
662. Maximum Width of Binary Tree
"""
from createBT import BTRoot

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.q1=[root]
        self.q2=[]
        self.width=[1]
        self.widths=[[1]]
        self.visit(self.q1, self.q2)
             
        return max(i[-1]-i[0]+1 for i in self.widths[:-1])
        
    def visit(self, q1, q2):
        if q1 == []:
            return
        while q1 != []:
            if q1[0].left: 
                q2.append(q1[0].left)
                self.width.append(self.width[0]*2)
            if q1[0].right: 
                q2.append(q1[0].right)
                self.width.append(self.width[0]*2+1)
            del q1[0]
            del self.width[0]

        self.widths.append(self.width[:])
        self.visit(q2, q1)

root = BTRoot([1,3,2,5,None,None,5]).get_root()
s = Solution().widthOfBinaryTree(root)