#pragma once
#include "ListNode.h"

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* sortedHead = new ListNode(0);
        ListNode* cur = sortedHead;
        while (l1 && l2) {
            if (l1->val <= l2->val) {
                cur->next = l1;
                l1 = l1->next;
                cur = cur->next;
            }
            else {
                cur->next = l2;
                l2 = l2->next;
                cur = cur->next;
            }
        }
        if (l1)
            cur->next = l1;
        else
            cur->next = l2;
        return sortedHead->next;
    }
};
