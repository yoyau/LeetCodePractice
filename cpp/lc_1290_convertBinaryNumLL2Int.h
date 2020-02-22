#pragma once
#include "ListNode.h"

class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int decimalVal = 0;
        while (head) {
            decimalVal = (decimalVal << 1) + head->val;
            head = head->next;
        }
        return decimalVal;
    }
};
