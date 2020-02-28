#pragma once
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int>::iterator l = numbers.begin(), r = numbers.end() - 1;
        int sum = *l+*r;
        while (1) {
            if (sum < target)
                sum = *++l+*r;
            else if (sum > target)
                sum = *--r+*l;
            else
                return vector<int>{l-numbers.begin()+1, r-numbers.begin()+1};
        }
    }
};
