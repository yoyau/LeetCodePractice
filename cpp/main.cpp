#include <iostream>
#include <vector>
#include "test.h"
#include "ListNode.h"
#include "lc_0011_containerWithMostWater.h"

using namespace std;
void scanLL(ListNode*);

int main()
{
    // creat linked list
    vector<int> v{ 2,3,4,5,18,17,6 };
    vector<ListNode> linkedL(v.size(), 10);
    creatLL(v, linkedL);

    vector<int> v2{ 5,6,4 };
    vector<ListNode> linkedL2(v2.size(), 10);
    creatLL(v2, linkedL2);

    // check content in linked list
    scanLL(&linkedL[0]);
    scanLL(&linkedL2[0]);
    cout << endl << "after fun" << endl;

    Solution s;
    int a = s.maxArea(v);
    // scanLL(&linkedL[0);
    return 0;
}

void scanLL(ListNode* head) {
    while (head->next) {
        cout << head->val << "->";
        head = head->next;
    }
    cout << head->val << endl;
}