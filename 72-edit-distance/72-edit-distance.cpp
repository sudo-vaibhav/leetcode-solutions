class Solution {
public:
    int solve(int i1, int i2, string word1,string word2,vector<vector<int>>& dp){
        if(dp[i1][i2]!=-1) return dp[i1][i2];
        if(i1==0 || i2==0){
            return max(i1,i2);
        }
        else{
            
            if(word1[i1-1]==word2[i2-1]){
                return dp[i1][i2] = solve(i1-1,i2-1,word1,word2,dp);
            }
            else{
                auto temp = vector<int>({
                    solve(i1-1,i2,word1,word2,dp),
                    solve(i1,i2-1,word1,word2,dp),
                    solve(i1-1,i2-1,word1,word2,dp)
                });
                return dp[i1][i2] = 1+ *min_element(temp.begin(),temp.end());
            }
        }
    }
    
    int minDistance(string word1, string word2) {
        vector<vector<int>> dp(word1.size()+1,vector<int>(word2.size()+1,-1));
        return solve(word1.size(),word2.size(),word1,word2,dp); 
    }
};