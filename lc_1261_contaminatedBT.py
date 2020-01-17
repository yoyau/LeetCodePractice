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
        root.val = 0
        self.recover(root)
        self.root = root
        
    def recover(self, node):
        if not node: return
        if node.left:
            node.left.val = 2*node.val+1
            self.recover(node.left)
        if node.right:
            node.right.val = 2*node.val+2
            self.recover(node.right)
            
    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        targetPath = [target]
        while target != 0:
            if target % 2 == 1:
                target = (target-1)/2
                targetPath.append(target)
            else:
                target=(target-2)/2
                targetPath.append(target)
        print(targetPath)
        currentNode = self.root
        for i in range(-2, -(len(targetPath))-1, -1):
            if currentNode.left and currentNode.left.val == targetPath[i]:
                currentNode = currentNode.left
            elif currentNode.right and currentNode.right.val == targetPath[i]:
                currentNode = currentNode.right
            else:
                return False
        return True
    
root = BTRoot([-1,None,-1,None,None,-1,None,-1]).get_root()
f = FindElements(root)
found = f.find(11)