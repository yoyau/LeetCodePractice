#pragma once
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        vector<int> square(A.size(), 0);
        vector<int>::iterator it=--square.end(), begin=A.begin(), end=--A.end();
        while (begin != end) {
            if ((*begin) * (*begin) > (*end)* (*end)) {
                *it = (*begin) * (*begin);
                ++begin;
                --it;
            }
            else {
                *it = (*end) * (*end);
                --end;
                --it;
            }
        }
        *it = (*end) * (*end);
        for (auto sq : square) {
            cout << sq << endl;
        }
        return square;
    }
};
