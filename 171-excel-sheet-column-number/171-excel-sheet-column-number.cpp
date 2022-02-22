class Solution {
public:
    int titleToNumber(string columnTitle) {
        int ans=0;
        // reverse(columnTitle.begin(),columnTitle.end());
        for(auto i : columnTitle){
            ans*=26;
            ans+=i-'A'+1;
        }
        return ans;
    }
};