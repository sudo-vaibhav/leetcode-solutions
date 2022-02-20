class Solution {
public:
    string longestPalindrome(string s) {
        string rev = s;
        int n = s.size();
        int ansI,ansJ;
        vector<vector<bool>> dp(n, vector<bool>(n,false));
        int result = 0;
        for(auto end=0;end<n;end++){
            for(auto start=0;start<=end;start++){
                auto compare = s[start]==s[end];
                dp[start][end] = compare&&(end-start>1 ? dp[start+1][end-1]:true);
                if(dp[start][end]){
                    if(end-start+1>result){
                        result = end-start+1;
                        ansI = start;
                        ansJ = end;
                    }
                }
            }
        }
        return s.substr(ansI, ansJ-ansI+1);
    }
};