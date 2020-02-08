#include <iostream>
#include "test.h"
#include "ListNode.h"
#include "lc_0206_reverseLinkedList.h"

using namespace std;
void scanLL(ListNode*);

int main()
{
    // creat linked list
    const int number = 5;
    int input[number] = { 1,2,3,4,5 };
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
    scanLL(s.reverseList(head));

    return 0;
}

void scanLL(ListNode* head) {
    while (head->next) {
        cout << head->val << endl;
        head = head->next;
    }
    cout << head->val;
}