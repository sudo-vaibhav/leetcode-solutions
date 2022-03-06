class Solution {
public:
    int minDistance(string word1, string word2) {
        vector<vector<int>> dp(word1.size()+1,vector<int>(word2.size()+1));
        for(int i1=0;i1<=word1.size();i1++){
            for(int i2=0;i2<=word2.size();i2++){
                if(i2==0) dp[i1][0] = i1;
                else if(i1==0) dp[0][i2] = i2;
                else if(word1[i1-1]==word2[i2-1]){
                    dp[i1][i2] = dp[i1-1][i2-1];
                }
                else{
                    auto op1 = dp[i1-1][i2], op2 = dp[i1][i2-1],
                        op3 = dp[i1-1][i2-1];
                    dp[i1][i2] = 1+ min(op1,min(op2,op3));
                }
            }
        }
        return dp[word1.size()][word2.size()]; 
    }
};