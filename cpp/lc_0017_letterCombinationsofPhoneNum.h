#pragma once
#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    void letterCombinations(string digits) {
        if (digits.empty()) return {};
        vector<string> map(8); // only 2-9 is possible
        map[0] = "abc";
        map[1] = "def";
        map[2] = "ghi";
        map[3] = "jkl";
        map[4] = "mno";
        map[5] = "pqrs";
        map[6] = "tuv";
        map[7] = "wxyz";
        
        vector<string> set;
        string cur;
        combinationSearch(digits, map, digits.size(), cur, 0, set);
    }
private:
    void combinationSearch(string &digits, vector<string>& map, int maxLength, string& cur, unsigned int s, vector<string>& set) {
        if (!maxLength) {
            set.push_back(cur);
            return;
        }
        for (char c : map[(digits[s]-'0')-2]) {
            cur.push_back(c);
            combinationSearch(digits, map, maxLength - 1, cur, s + 1, set);
            cur.pop_back();
        }
    }
};
