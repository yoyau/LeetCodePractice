# -*- coding: utf-8 -*-
"""
1104. Path In Zigzag Labelled Binary Tree
"""

class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        if label == 1: return [1]
        l = label
        # find current level
        level = 1
        while label != 1:
            if label % 2 == 1:
                label = (label-1)/2
                level+=1
            else:
                label=label/2
                level+=1

        # append initial label first
        path = [l]
        if level % 2 == 0:       
            newNodes = list(range(2**(level-1), 2**level))
            l = newNodes[-(newNodes.index(l)+1)]
        l = l // 2
        level-=1

        while l != 1:
            if level % 2 == 1:
                path.append(l)
                l = l // 2
                level-=1
            else:
                newNodes = list(range(2**(level-1), 2**level))
                l_zig = newNodes[-(newNodes.index(l)+1)]
                path.append(l_zig)
                l = l // 2
                level-=1
                
        path.append(1)
        path.reverse()
        return path
        
s = Solution()
l = s.pathInZigZagTree(15)