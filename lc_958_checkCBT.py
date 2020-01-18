# -*- coding: utf-8 -*-
"""
958. Check Completeness of a Binary Tree
"""
from createBT import BTRoot

class Solution:
    def isCompleteTree(self, root) -> bool:
        if not root: return
        self.oneChild=False
        return self.visit([root], [])
             
    def visit(self, q1, q2):
        if q1 == []:
            return True

        while q1 != []:
            if q1[0].left and q1[0].right: 
                if self.oneChild:
                    return False 
                q2.append(q1[0].left)
                q2.append(q1[0].right)
            elif q1[0].left:
                if self.oneChild:
                    return False
                q2.append(q1[0].left)
                self.oneChild=True
            elif q1[0].right:
                return False
            else:
                self.oneChild=True
            del q1[0]
        return self.visit(q2, q1)

root = BTRoot([1,2,3,5,None,7]).get_root()
s = Solution()
steps = s.isCompleteTree(root)