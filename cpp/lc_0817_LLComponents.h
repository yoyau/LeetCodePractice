#pragma once
#include "ListNode.h"
#include <unordered_set>

class Solution {
public:
    int numComponents(ListNode* head, vector<int>& G) {
        int num = 0;
        unordered_set<int> setG(G.begin(), G.end());
        while (head) {
            // detect boundary, if first in G and second not in G -> ++num
            //                     first in G and no secont -> ++ num
            if (setG.count(head->val) && (!(head->next) || !(setG.count(head->next->val)))) {
                ++num;
            }
            head = head->next;
        }
        return num;
    }
};
