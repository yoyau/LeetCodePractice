# -*- coding: utf-8 -*-
"""
979. Distribute Coins in Binary Tree
"""

from createBT import BTRoot

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return
        self.steps = 0
        self.coinsCount(root)
        return self.steps
    
    def coinsCount(self, node):
        if not node: return 0
        left = self.coinsCount(node.left)
        right = self.coinsCount(node.right)
        self.steps += abs((node.val-1) + left + right) 
        return (node.val-1) + left + right
        

root = BTRoot([1,0,2]).get_root()
s = Solution()
steps = s.distributeCoins(root)