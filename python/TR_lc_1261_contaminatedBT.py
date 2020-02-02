# -*- coding: utf-8 -*-
"""
1261. Find Elements in a Contaminated Binary Tree
"""

from createBT import BTRoot

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if not root: return
        self.root = root
            
    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        path = []
        while target != 0:
            if target % 2 == 1:
                path.append('L')
                target = (target-1)/2
            else:
                path.append('R')
                target = (target-2)/2
        
        c = self.root
        while len(path):
            direction = path[-1]
            if direction == 'L':
                if not c.left: 
                    return False
                else:
                    c = c.left
                    del path[-1]
            else:
                if not c.right:
                    return False
                else:
                    c = c.right
                    del path[-1]
        return True
            
    
root = BTRoot([-1,None,-1,None,None,-1,None]).get_root()
f = FindElements(root)
found = f.find(2)