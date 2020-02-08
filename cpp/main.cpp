#include <iostream>
#include "test.h"
#include "ListNode.h"
#include "lc_0234_palindromeLinkedList.h"

using namespace std;
void scanLL(ListNode*);

int main()
{
    // creat linked list
    const int number = 5;
    int input[number] = { 1, 2, 1,2,1};

    ListNode start(input[0]);
    ListNode* head = &start;
    ListNode* ptr = &start;

    for (int i = 1;i < number;i++)
    {
        ptr->next = new ListNode(input[i]);
        ptr = ptr->next;
    }

    // check content in linked list
    //scanLL(head);

    Solution s;
    cout << s.isPalindrome(head);

    return 0;
}

void scanLL(ListNode* head) {
    while (head->next) {
        cout << head->val << endl;
        head = head->next;
    }
    cout << head->val;
}