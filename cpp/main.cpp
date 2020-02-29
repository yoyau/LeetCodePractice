#include <iostream>
#include <vector>
#include "test.h"
#include "ListNode.h"
#include "lc_0784_letterCasePermutation.h" 
using namespace std;

void scanLL(ListNode*);
void scanVV(vector<vector<int>>&);

int main()
{
    // creat linked list
    vector<int> v{ 1,1,2 };
    vector<ListNode> linkedL(v.size(), 10);
    creatLL(v, linkedL);

    vector<int> v2{ 3,33,333 };
    vector<ListNode> linkedL2(v2.size(), 10);
    creatLL(v2, linkedL2);

    // check content in linked list
    scanLL(&linkedL[0]);
    scanLL(&linkedL2[0]);
    cout << endl << "after fun" << endl;

    Solution s;
    vector<string> a = s.letterCasePermutation("C");
    //scanVV(a);

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

void scanVV(vector<vector<int>>& vec) {
    for (auto v : vec) {
        cout << "[";
        for (auto e : v) {
            cout << e << ", ";
        }
        cout << "]" << endl;
    } 
}