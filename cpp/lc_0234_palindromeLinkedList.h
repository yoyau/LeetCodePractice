#pragma once
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        // determine mid point
        ListNode* first = head, * second = head;
        while (second && second->next) {
            first = first->next;
            second = second->next->next;
        }

        // reverse second part of the LL
        first = reverseList(first);

        // compare second(reversed first) and first(head)
        while (first) {
            if (first->val != head->val) 
                return false;
            else {               
                first = first->next;
                head = head->next;             
            }
        }
        return true;
    }
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