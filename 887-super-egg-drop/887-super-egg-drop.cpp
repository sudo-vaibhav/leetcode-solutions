// class Solution:
//     def superEggDrop(self, k: int, n: int) -> int:
//         @cache
//         def solve(eggs,floors):
//             if(eggs==1 or floors<=1): return floors
//             ans = float("inf")
//             for k in range(1,floors+1):
//                 tempans = 1+max(solve(eggs-1,k-1),solve(eggs,floors-k))
//                 ans = min(ans,tempans)
//             return ans
        
//         return solve(k,n)
class Solution {
public:
    int dp[105][10005];
    int solve(int eggs,int floors){
        
        
        if(eggs==1 || floors<=1) return dp[eggs][floors]=floors;
        if(dp[eggs][floors]!=-1)return dp[eggs][floors];
        int ans = floors;
        auto l = 1,r=floors;
        while(l<=r){
            auto m =(r+l)/2;
            auto left = solve(eggs-1,m-1);
            auto right = solve(eggs,floors-m);
            ans = min(ans, 1+max(left,right));
            if(left<right){
                l=m+1;
            }
            else{
                r=m-1;
            }
        }
        return dp[eggs][floors]=ans;
    }
    int superEggDrop(int eggs, int floors) {
        memset(dp,-1,sizeof(dp));
        return solve(eggs,floors);
    }
};