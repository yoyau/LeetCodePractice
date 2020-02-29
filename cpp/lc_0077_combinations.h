#pragma once
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> set;
        vector<int> cur;
        vector<int> candidates(n, 0);
        for (int i = 0;i < n;++i) {
            candidates[i] = i + 1;
        }
        combinationSearch(candidates, k, cur, 0, set);
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
