class Solution {
public:
    int dp[305][305];
    bool solve(int start, int end,string&s,  unordered_set<string>&words){
        if(start>end) return 1;
        if(dp[start][end]!=-1) return dp[start][end];
            for(auto END=start;END<=end;END++){
                auto substring = s.substr(start,END-start+1);
                if(
                    words.count(substring)
                    && solve(END+1,end,s,words)
                ){
                    return dp[start][end]=1;
                }
                
            }        
        return dp[start][end]=0;
    }
    bool wordBreak(string s, vector<string>& wordDict) {
        memset(dp,-1,sizeof(dp));
        unordered_set<string> words(wordDict.begin(),wordDict.end());
        return solve(0,s.size()-1,s,words);
    }
};