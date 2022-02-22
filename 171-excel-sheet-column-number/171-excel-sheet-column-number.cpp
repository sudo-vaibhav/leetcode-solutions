class Solution {
public:
    int titleToNumber(string columnTitle) {
        long ans=0;
        for(auto i : columnTitle) ans=ans*26+i-'A'+1;
        return ans;
    }
};