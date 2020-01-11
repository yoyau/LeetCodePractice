# -*- coding: utf-8 -*-
"""
654. Maximum Binary Tree
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            val, ind= max(nums), nums.index(max(nums))
            t = TreeNode(val)
            t.left = self.constructMaximumBinaryTree(nums[:ind])
            t.right = self.constructMaximumBinaryTree(nums[ind+1:])
            return t

input_ = [3,2,1,6,0,5]
s = Solution()
root = s.constructMaximumBinaryTree(input_)