#pragma once
#include "ListNode.h"
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> decompressedList;
        for (int i = 0; i < nums.size(); i+=2) {
            decompressedList.insert(decompressedList.end(), nums[i], nums[i + 1]);
        }
        return decompressedList;
    }
};
