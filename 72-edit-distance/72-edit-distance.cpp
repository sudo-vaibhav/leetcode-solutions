class Solution {
public:
//     int solve(int i1, int i2, string word1,string word2,vector<vector<int>>& dp){
//         if(dp[i1][i2]!=-1) return dp[i1][i2];
//         if(i1==0 || i2==0){
//             return max(i1,i2);
//         }
//         else{
            
//         }
//     }
    
    int minDistance(string word1, string word2) {
        vector<vector<int>> dp(word1.size()+1,vector<int>(word2.size()+1,-1));
        for(auto i=0;i<=word1.size();i++){
            dp[i][0] = i;
        }
        for(auto i=0;i<=word2.size();i++){
            dp[0][i] = i;
        }
        for(int i1=1;i1<=word1.size();i1++){
            for(int i2=1;i2<=word2.size();i2++){
                if(word1[i1-1]==word2[i2-1]){
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