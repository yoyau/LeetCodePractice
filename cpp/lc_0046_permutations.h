#pragma once
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> set;
        vector<int> cur;
        vector<bool> used(nums.size(), 0);
        std::sort(nums.begin(), nums.end());
        permutationSearch(nums, nums.size(), cur, used, set);
        return set;
    }

private:
    void permutationSearch(vector<int>& candidates, int maxLength, vector<int>& cur, vector<bool>& used, vector<vector<int>>& set) {
        if (!maxLength) {
            set.push_back(cur);
            return;
        }
        for (unsigned int i = 0;i < candidates.size();++i) {
            if (used[i])
                continue;
            cur.push_back(candidates[i]);
            used[i] = 1;
            permutationSearch(candidates, maxLength - 1, cur, used, set);
            cur.pop_back();
            used[i] = 0;
        }
    }
};

