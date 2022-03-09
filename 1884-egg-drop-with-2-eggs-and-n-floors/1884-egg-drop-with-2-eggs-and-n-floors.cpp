class Solution {
public:
    int dp[3][1005];
    int solve(int eggs,int floors){
        if(dp[eggs][floors]!=-1)return dp[eggs][floors];
        if(eggs==1 || floors<=1) return dp[eggs][floors]=floors;
        int ans = floors;
        for(int k=1;k<=floors;k++){
            ans = min(ans, 1+max(solve(eggs-1,k-1),solve(eggs,floors-k)));
        }
        return dp[eggs][floors]=ans;
    }
    int twoEggDrop(int n) {
        memset(dp,-1,sizeof(dp));
        return solve(2,n);
    }
};