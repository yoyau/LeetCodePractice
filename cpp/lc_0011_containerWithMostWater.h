#pragma once
#include <vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        vector<int>::iterator lb = height.begin(), rb = height.end() - 1;
        int volume = 0;
        while (lb != rb) {
            volume = (volume > ((*lb < *rb ? *lb : *rb) * (rb - lb))) ? volume : ((*lb < *rb ? *lb : *rb) * (rb - lb));
            if (*lb < *rb) ++lb;
            else --rb;
            cout << volume << endl;
        }
        return volume;
    }
};
