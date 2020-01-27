# -*- coding: utf-8 -*-
"""
108. Convert Sorted Array to Binary Search Tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []: return
        if len(nums) == 1: return TreeNode(nums[0])
        mid = int(len(nums)/2)
        top_root = TreeNode(nums[mid])
        self.buildBST(top_root, nums[0:mid], nums[mid+1:])
        return top_root
    
    def buildBST(self, root, left, right):
        if len(left) == 1:
            if len(right) == 1:
                root.left = TreeNode(left[0])
                root.right = TreeNode(right[0])          
            elif right == []:   
                root.left = TreeNode(left[0])
            else:
                root.left = TreeNode(left[0])
                root.right = TreeNode(right[1])
                root.right.left = TreeNode(right[0])
                
        elif left == []:
            if len(right) == 1:
                root.right = TreeNode(right[0])
  
        else:
            l_mid = int(len(left)/2)
            r_mid = int(len(right)/2)
            root.left = TreeNode(left[l_mid])
            root.right = TreeNode(right[r_mid])
            self.buildBST(root.left, left[0:l_mid], left[l_mid+1:])
            self.buildBST(root.right, right[0:r_mid], right[r_mid+1:])
            
        
nums = [-1,0,1,2]
s = Solution()
t = s.sortedArrayToBST(nums)