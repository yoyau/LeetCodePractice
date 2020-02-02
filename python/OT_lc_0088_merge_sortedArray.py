# -*- coding: utf-8 -*-
"""
88. Merge Sorted Array
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # just fill the nums1's slots from tail
        while m and n:
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n=n-1
            else:
                nums1[m+n-1] = nums1[m-1]
                m=m-1
        if m == 0:
            nums1[0:n]=nums2[0:n]
        print(nums1)


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]    
s = Solution()
s.merge(nums1, 3, nums2, 3)