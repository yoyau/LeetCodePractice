#pragma once
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <set>
using namespace std;

class Solution {
public:
    // In combinationSum_I, the element in candidates could be repeated unlimited.
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> set;
        vector<int> cur;
        std::sort(candidates.begin(), candidates.end());
        combinationSearch(candidates, target, cur, 0, set);
        return set;
    }
    //
    // In combinationSum_II, the element in candidates could "not" be repeated unlimited.
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> set;
        vector<int> cur;
        std::sort(candidates.begin(), candidates.end());
        combinationSearch(candidates, target, cur, 0, set);
        std::set<vector<int>> uni(set.begin(), set.end());
        set.assign(uni.begin(), uni.end());
        return set;
    }
    //
    // In combinationSum_III, the length of the combinatio is limited.
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> set;
        vector<int> cur, candidates{ 1,2,3,4,5,6,7,8,9 };
        combinationSearch(candidates, n, k, cur, 0, set);
        return set;
    }
    //
    // In combination_VI, the same elements combination with different order is considered as different solution.
    // Only ask the "number" of the solution -> DP problem.
    int combinationSum4(vector<int>& nums, int target) {
        vector<int> sol(target + 1, -1);
        sol[0] = 1;
        return helper(nums, target, sol);
    }
    int helper(vector<int>& nums, int target, vector<int> & sol) {
        if (target < 0) return 0;
        if (sol[target] != -1) return sol[target];
        int ans = 0;
        for (auto n : nums) {
            ans += helper(nums, target - n, sol);
        }
        return sol[target] = ans;
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
            combinationSearch(candidates, target - candidates[s], cur, s, set);
            cur.pop_back();
        }
    }
    void combinationSearch(vector<int>& candidates, int target, int maxLength, vector<int> &cur, unsigned int s, vector<vector<int>> &set) {
        if (!maxLength) {
            if (!target) 
                set.push_back(cur);
        return;
        }
        for (s;s < candidates.size();++s) {
            if (candidates[s] > target) break;
            cur.push_back(candidates[s]);
            combinationSearch(candidates, target - candidates[s], maxLength-1, cur, s+1, set);
            cur.pop_back();
        }
    }
};
