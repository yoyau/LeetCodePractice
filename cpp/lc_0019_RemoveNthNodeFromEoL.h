#pragma once
#include "ListNode.h"

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* cur = new ListNode(0), * n_next = cur;
        cur->next = head;
        head = cur;
        while (n) {
            n -= 1;
            n_next = n_next->next;
        }
        n_next = n_next->next;
        while (n_next) {
            cur = cur->next;
            n_next = n_next->next;
        }
        cur->next = cur->next->next;
        return head->next;
    }
};
