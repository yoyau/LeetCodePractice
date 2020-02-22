#include <iostream>
#include "test.h"
#include "ListNode.h"
#include "lc_0203_removeLinkedListElements.h"

using namespace std;
void scanLL(ListNode*);

int main()
{
    // creat linked list
    const int number = 7;
    int input[number] = { 1, 2, 6, 3, 4, 5, 6};

    ListNode start(input[0]);
    ListNode* head = &start;
    ListNode* ptr = &start;

    for (int i = 1;i < number;i++)
    {
        ptr->next = new ListNode(input[i]);
        ptr = ptr->next;
    }

    // check content in linked list
    scanLL(head);
    cout << endl << "after remove fun" << endl;

    
    Solution s;
    head = s.removeElements(head, 6);

    scanLL(head);
    return 0;
}

void scanLL(ListNode* head) {
    while (head->next) {
        cout << head->val << "->";
        head = head->next;
    }
    cout << head->val << endl;
}