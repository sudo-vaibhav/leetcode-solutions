class Solution {
public:
    int minimumWhiteTiles(string fl, int nc, int cl) {
        int n = fl.size();
        vector<vector<int>>dp(n+1,vector<int>(nc+1,0));
        for(int floorLen=1;floorLen<=n;floorLen++){
            for(int carpHave=0;carpHave<=nc;carpHave++){
                auto cover = carpHave ? dp[max(floorLen-cl,0)][carpHave-1]:INT_MAX;
                auto notcover = fl[floorLen-1]-'0' + dp[floorLen-1][carpHave];
                dp[floorLen][carpHave] = min(cover,notcover);
            }
        }
        
        return dp[n][nc];
        
    }
};