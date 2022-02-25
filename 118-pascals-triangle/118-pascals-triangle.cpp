// power of 11 approach, won't work for large n values due to overflow
// class Solution {
// public:
//     vector<vector<int>> generate(int n) {
//         vector<vector<int>> res;
//         for(int i=0;i<n;i++){
//             vector<int> ans;
//             auto temp  = (int)pow(11,i);
//             while(temp){
//                 auto digit = temp%10;
//                 temp/=10;
//                 ans.push_back(digit);
//             }
//             res.push_back(ans);
//         }
//         return res;
//     }
// };

// combination / binomial theorem approach
// class Solution{
//     unsigned long long fact(int n, unordered_map<int,unsigned long long>& dp){
//         if(n==0) return 1;
//         if(dp.count(n)) return dp[n];
//         return dp[n] = fact(n-1,dp)*n;
//     }
//     unsigned long long iCj(int i,int j, unordered_map<int,unsigned long long>& dp){
//         // n!/k!*(n-k)!
//         return fact(i,dp)/(fact(j,dp)*fact(i-j,dp));
//     }
//     public:
//     vector<vector<int>> generate(int n){
//         vector<vector<int> > res;
//          unordered_map<int,unsigned long long> dp;
//         for(int i=0;i<n;i++){
//             vector<int> temp;
//             for(int j=0;j<=i;j++){
//                 temp.push_back(iCj(i,j,dp));
//             }
//             res.push_back(temp);
//         }
//         return res;
//     }
// };

class Solution{
    public:
    vector<vector<int>> generate(int n){
        vector<vector<int>> res = {{1}};
        for(int i=0;i<n-1;i++){
            vector<int> temp;
            int prevSize = res.back().size();
            vector<int> prev = res.back();
            for(int j=0;j<prevSize+1;j++){
                int t1 = j-1>=0 ? prev[j-1] : 0;
                int t2 = j < prevSize ? prev[j]:0;
                temp.push_back(t1+t2);
            }
            res.push_back(temp);
        }
        
        return res;
    }
};