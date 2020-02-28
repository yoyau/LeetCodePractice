#pragma once
#include "ListNode.h"

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            head = head->next;
            fast = fast->next->next;
        }
        if (fast->next) return head->next;
        else return head;
    }
};
