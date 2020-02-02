# -*- coding: utf-8 -*-
"""
21. Merge Two Sorted Lists
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        mergedList = ListNode(-1)
        cur = mergedList
        while True:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                if l1.next == None:
                    cur.next = l2
                    return mergedList.next
                else:
                    l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                if l2.next == None:
                    cur.next = l1
                    return mergedList.next
                else:
                    l2=l2.next
