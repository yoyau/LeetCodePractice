#pragma once
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <set>

class Solution {
public:
    // In combinationSum_I, the element in candidates could be repeated unlimited.
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> set;
        vector<int> cur;
        unsigned int start = 0;
        std::sort(candidates.begin(), candidates.end());
        combinationSearch(candidates, target, cur, start, set);
        return set;
    }
    //
    // In combinationSum_II, the element in candidates could "not" be repeated unlimited.
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> set;
        vector<int> cur;
        int start = 0;
        std::sort(candidates.begin(), candidates.end());
        combinationSearch(candidates, target, cur, start, set);
        std::set<vector<int>> uni(set.begin(), set.end());
        set.assign(uni.begin(), uni.end());
        return set;
    }
    //
    // In combinationSum_III, the length of the combinatio is limited.
    vector<vector<int>> combinationSum3(vector<int>& candidates, int target) {
        vector<vector<int>> set;
        vector<int> cur;
        int start = 0;
        std::sort(candidates.begin(), candidates.end());
        combinationSearch(candidates, target, cur, start, set);
        std::set<vector<int>> uni(set.begin(), set.end());
        set.assign(uni.begin(), uni.end());
        return set;
    }

private:
    void combinationSearch(vector<int>& candidates, int target, vector<int> &cur, unsigned int s, vector<vector<int>> &set) {
        if (!target) {
            set.push_back(cur);
            return;
        }
        for (s;s < candidates.size();++s) {
            if (candidates[s] > target) break;
            cur.push_back(candidates[s]);
            combinationSearch(candidates, target - candidates[s], cur, s+1, set);
            cur.pop_back();
        }
    }
};
