#pragma once
#include "ListNode.h"

class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode* fast = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            head = head->next;
            if (fast == head)
                return 1;
        }
        return 0;
    }
    // 142. detect the beginning of the cycle
    ListNode* detectCycle(ListNode* head) {
        ListNode* fast = head, *slow = head;
        bool isCycle = 0;
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow) {
                isCycle = 1;
                break;
            }
        }
        if (!isCycle) return 0;
        while (head != slow) {
            head = head->next;
            slow = slow->next;
        }
        return slow;
    }
};
