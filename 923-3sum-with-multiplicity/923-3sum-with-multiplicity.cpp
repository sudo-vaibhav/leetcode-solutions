class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        int mod = 1000000007;
        int n = arr.size();
        auto s = set(arr.begin(),arr.end());
        int dp[n+1][101];
        for(int i=0;i<101;i++){
            dp[0][i] = 0;
        }
        for(int i=1;i<=n;i++){
            for(auto v:s){
                dp[i][v] = dp[i-1][v];
                if(v==arr[i-1]){
                    dp[i][v] = dp[i][v]+1;
                }
            }
        }
        int ans = 0;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int leftOver = target-arr[i]-arr[j];
                if(leftOver>=0 && leftOver<=100 && s.count(leftOver)){
                    ans += dp[n][leftOver]-dp[j+1][leftOver];
                    if(ans>=mod){ans-=mod;}
                }
            }
        }
        return ans;
    }
};