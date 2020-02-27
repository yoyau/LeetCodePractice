#pragma once
#include "ListNode.h"

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head) return head;
        ListNode* o_e = head, * o_c = head, *e_b = head->next, *e_e = head->next;
        while (e_e && e_e->next) {
            o_c = e_e->next;
            o_e->next = o_c;
            e_e->next = o_c->next;
            o_c->next = e_b;
            o_e = o_e->next;
            e_e = e_e->next;
        }
        return head;
    }
};
