#pragma once
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
     void getPermutation(int n, int k) {
        string cur;
        int curNum = 0;
        vector<bool> used(n, 0);
        combinationSearch(n, k, n, used, curNum, cur);
        cout << cur << endl;
        //return set;
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
