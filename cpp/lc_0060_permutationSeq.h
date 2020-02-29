#pragma once
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
     string getPermutation(int n, int k) {
        string cur;
        int curNum = 0;
        vector<bool> used(n, 0);
        combinationSearch(n, k, n, used, curNum, cur);
        return cur;
     }
     // undone
     string getPermutation_quick(int n, int k) {
         string sol, candidates("0123456789");
         vector<int> fact(n, 0);
         fact[0] = 1;
         int fixed;
         for (int i = 1;i < n;++i) {
             fact[i] = (i+1) * fact[i - 1];
             if (fact[i] > k) {
                 fixed = fact[i-1];
                 break;
             }
         }
         sol.push_back(candidates[k / fixed]);
     }

private:
    void combinationSearch(int maxLength, int k, int depth, vector<bool> &used, int&curNum, string& cur) {
        if (!depth) {
            curNum += 1;
            return;
        }
        for (unsigned int i=0;i <maxLength;++i) {
            if (curNum == k) break;
            if (used[i]) continue;
            cur.push_back((char)(i+49));
            used[i] = 1;
            combinationSearch(maxLength, k, depth-1, used, curNum, cur);
            if (curNum == k) break;
            cur.pop_back();
            used[i] = 0;
        }
    }
};
