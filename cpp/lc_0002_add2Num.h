#pragma once
#include "ListNode.h"
#include<iostream>
using namespace std;

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int rem = 0, sum = 0;
        ListNode* cur = new ListNode(0), * head = cur;
        while (l1 || l2 || rem) {
            sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + rem;
            cur->next = new ListNode(sum % 10);
            rem = (sum - sum % 10) / 10;
            cur = cur->next;
            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
        }
        return head->next;
    }
};
