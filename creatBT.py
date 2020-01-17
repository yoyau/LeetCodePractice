# -*- coding: utf-8 -*-
"""
Create Binary Tree (for testing)
"""
import numpy as np

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class BTRoot:
    def __init__(self, nodeValList):
        
        while len(nodeValList) < 2**(np.ceil(np.log2(len(nodeValList)+1)))-1:
            nodeValList += [None]
                 
        self.nodeDic = {}
        for i in range(len(nodeValList)):
            if nodeValList[i]:
                self.nodeDic['TreeNode_'+str(i)]=TreeNode(nodeValList[i])
            else:
                self.nodeDic['TreeNode_'+str(i)]=None

        maxLevel = int(np.log2(len(nodeValList)+1)-1)
        for i in range(2**(maxLevel)-1):
            if self.nodeDic['TreeNode_'+str(i)]:
                self.nodeDic['TreeNode_'+str(i)].left = self.nodeDic['TreeNode_'+str(2*i+1)]
                self.nodeDic['TreeNode_'+str(i)].right = self.nodeDic['TreeNode_'+str(2*i+2)]
            
    def get_root(self):
        return self.nodeDic['TreeNode_0']

            
        
