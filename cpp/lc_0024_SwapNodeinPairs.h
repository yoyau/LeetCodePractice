#pragma once
#include "ListNode.h"

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* pre = new ListNode(0), *next, *cur;
        pre->next = head;
        head = pre;
        while (pre->next && pre->next->next) {
            cur = pre->next;
            next = pre->next->next;
            next = next->next;
            pre->next = cur->next;
            pre->next->next = cur;
            cur->next = next;
            pre = pre->next->next;
        }
        return head->next;
    }
};
