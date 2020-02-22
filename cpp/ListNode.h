#pragma once
#include <vector>
using namespace std;
// Definition for singly - linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(0) {}
};

void creatLL(vector<int> &v, vector<ListNode> &ll) {
    const int length = v.size();
    for (int i = 0;i < length;i++)
    {
        ll[i].val = v[i];
        if (i == length - 1)
            break;
        ll[i].next = &ll[i + 1];
    }
}
