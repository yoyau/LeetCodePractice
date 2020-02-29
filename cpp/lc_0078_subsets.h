#pragma once
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> set;
        vector<int> cur;
        std::sort(nums.begin(), nums.end());
        for (unsigned int k = 0;k <= nums.size();++k) {
            combinationSearch(nums, k, cur, 0, set);
        }
        return set;
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> set;
        vector<int> cur;
        std::sort(nums.begin(), nums.end());
        for (unsigned int k = 0;k <= nums.size();++k) {
            combinationSearch(nums, k, cur, 0, set);
        }
        std::set<vector<int>> uniSet;
        for (unsigned int i = 0; i < set.size(); ++i) {
            uniSet.insert(set[i]);
        }
        set.assign(uniSet.begin(), uniSet.end());
        return set;
    }

private:
    void combinationSearch(vector<int>& candidates, int maxLength, vector<int>& cur, unsigned int s, vector<vector<int>>& set) {
        if (!maxLength) {
            set.push_back(cur);
            return;
        }
        for (s;s < candidates.size();++s) {
            cur.push_back(candidates[s]);
            combinationSearch(candidates, maxLength - 1, cur, s + 1, set);
            cur.pop_back();
        }
    }
};
