# -*- coding: utf-8 -*-
"""
654. Maximum Binary Tree
"""

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        ind, val = max(nums), nums.index(max(nums))
        l=self.constructMaximumBinaryTree()