class Solution {
public:
    int minDistance(string word1, string word2) {
        vector<vector<int>> dp(word1.size()+1,vector<int>(word2.size()+1,-1));
        for(int i1=0;i1<=word1.size();i1++){
            for(int i2=0;i2<=word2.size();i2++){
                if(i2==0) dp[i1][0] = i1;
                else if(i1==0) dp[0][i2] = i2;
                else if(word1[i1-1]==word2[i2-1]){
                    dp[i1][i2] = dp[i1-1][i2-1];
                }
                else{
                    auto temp = vector<int>({
                        dp[i1-1][i2],
                        dp[i1][i2-1],
                        dp[i1-1][i2-1]
                    });
                    dp[i1][i2] = 1+ *min_element(temp.begin(),temp.end());
                }
            }
        }
        return dp[word1.size()][word2.size()]; 
    }
};