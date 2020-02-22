#include <iostream>
#include <vector>
#include "test.h"
#include "ListNode.h"
#include "lc_0160_intersectionof2LL.h"

using namespace std;
void scanLL(ListNode*);

int main()
{
    // creat linked list
    vector<int> v{ 3,2,4 };
    vector<ListNode> linkedL(v.size(), 10);
    creatLL(v, linkedL);

    vector<int> v2{ 0,9,1,2,4 };
    vector<ListNode> linkedL2(v2.size(), 10);
    creatLL(v2, linkedL2);

    // check content in linked list
    scanLL(&linkedL[0]);
    scanLL(&linkedL2[0]);
    cout << endl << "after fun" << endl;

    Solution s;
    ListNode* l = s.getIntersectionNode(&linkedL2[0], &linkedL[0]);
    //scanLL(l);
    //cout << l->val << endl;
    return 0;
}

void scanLL(ListNode* head) {
    while (head->next) {
        cout << head->val << "->";
        head = head->next;
    }
    cout << head->val << endl;
}