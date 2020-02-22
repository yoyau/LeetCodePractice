#pragma once

#include "ListNode.h"
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if (!head) return 0;
        head->next = removeElements(head->next, val);
        return (head->val == val) ? head->next : head;
    }
};
