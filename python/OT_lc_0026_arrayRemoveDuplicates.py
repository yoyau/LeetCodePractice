# -*- coding: utf-8 -*-
"""
26. Remove Duplicates from Sorted Array
"""

#nums = [1,1,2]
nums =[0,0,1,1,1,2,2,3,3,4]


l=len(nums)
if l==1:
    pass
else:
    a=0
    b=1
    while a<l-1:
        if (nums[a]<nums[b]):
            nums[a+1] = nums[b]
            if b==l-1:
                a+=1
                break
            else:    
                a+=1      
        else:
            if b==l-1:
                break
            b+=1