#include <iostream>
#include <vector>
#include "test.h"
#include "ListNode.h"
#include "lc_0021_merge2SortedLists.h"

using namespace std;
void scanLL(ListNode*);

int main()
{
    // creat linked list
    vector<int> v{ 1,2,4 };
    vector<ListNode> linkedL(v.size(), 10);
    creatLL(v, linkedL);

    vector<int> v2{ 1,3,4 };
    vector<ListNode> linkedL2(v.size(), 10);
    creatLL(v2, linkedL2);

    // check content in linked list
    scanLL(&linkedL[0]);
    scanLL(&linkedL2[0]);
    cout << endl << "after fun" << endl;

    Solution s;
    ListNode* l = s.mergeTwoLists(&linkedL[0], &linkedL2[0]);

    scanLL(l);
    return 0;
}

void scanLL(ListNode* head) {
    while (head->next) {
        cout << head->val << "->";
        head = head->next;
    }
    cout << head->val << endl;
}