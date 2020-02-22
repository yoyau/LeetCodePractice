#pragma once
#include "ListNode.h"

class Solution {
public:
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
        if (!headA || !headB)
            return 0;
        ListNode* indA = headA;
        ListNode* indB = headB;
        while (indA != indB) {
            indA = (indA ? indA->next : headB);
            indB = (indB ? indB->next : headA);
        }
        return indA;
    }
};
