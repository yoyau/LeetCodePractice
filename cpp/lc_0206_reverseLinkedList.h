#pragma once

#include <iostream>
//#include "ListNode.h"
using namespace std;


//ListNode head;

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head) {
            ListNode* next = head->next, * newHead = head;
            newHead->next = 0;
            while (next) {
                newHead = next;
                next = next->next;
                newHead->next = head;
                head = newHead;
            }
        }
        return head;
    }
};