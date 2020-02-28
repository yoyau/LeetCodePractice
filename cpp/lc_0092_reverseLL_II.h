#pragma once
#include "ListNode.h"

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        // creat dummy ListNode to include head
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        head = dummy;
        ListNode* begin = head, *end = head;
        for (int i = 0; i < (n - m + 2); i++) {
            end = end->next;
        }
        for (int i = 0; i < (m-1); i++) {
            begin = begin->next;
            end = end->next;
        }
        // reverse the List between "begin" and "end"
        reverseList(begin, end);
        return head->next;
    }

    void reverseList(ListNode* begin, ListNode* end) {
        ListNode* head = begin->next, * next = head->next, * newHead = head;
        newHead->next = end;
        while (next!=end) {
            newHead = next;
            next = next->next;
            newHead->next = head;
            head = newHead;
        }
        begin->next = head;
    }
};
