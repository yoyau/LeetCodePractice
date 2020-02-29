#pragma once
#include <vector>
#include <algorithm>
#include <set>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> letterCasePermutation(string S) {
        vector<string> set;
        string cur;
        permutationSearch(S, S.size(), cur, 0, set);
        return set;
    }
private:
    void permutationSearch(string& candidates, int maxLength, string& cur, unsigned int s, vector<string> &set) {
        if (!maxLength) {
            set.push_back(cur);
            cout << cur << endl;
            return;
        }
        cur.push_back(candidates[s]);
        permutationSearch(candidates, maxLength - 1, cur, s+1, set);
        cur.pop_back();

        if (candidates[s] >= 97) {
            cur.push_back((char)(candidates[s]-'a'+'A'));
            permutationSearch(candidates, maxLength - 1, cur, s+1, set);
            cur.pop_back();
        }
        else if (candidates[s] >= 65) {
            cur.push_back((char)(candidates[s]-'A'+'a'));
            permutationSearch(candidates, maxLength - 1, cur, s+1, set);
            cur.pop_back();
        }
    }
};
