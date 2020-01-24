# -*- coding: utf-8 -*-
"""
1290. Convert Binary Number in a Linked List to Integer
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
         
class Solution:
    def getDecimalValue(self, head):
        self.numInBinary=[]
        self.visit(head)
        L = len(self.numInBinary)
        o=0
        for ind, i in enumerate(self.numInBinary):
            if i == 1:
                o +=2**(L-ind-1)
        return o
    def visit(self, node):
        if not node: return
        self.numInBinary.append(node.val)
        self.visit(node.next)
        

head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)

r = Solution().getDecimalValue(head)