class Solution {
public:
    int DP(int a, int b, string& word1, string& word2, vector<vector<int>>& dp_arr){
        if(dp_arr[a][b]!=-1)return dp_arr[a][b];
        if(a==0 || b==0)return dp_arr[a][b]=a+b;
        else if(word1[a-1]==word2[b-1]){
            return dp_arr[a][b]=
                DP(a-1, b-1, word1, word2, dp_arr);
        }
        return dp_arr[a][b]=1+min(
            DP(a-1, b, word1, word2, dp_arr),
            DP(a, b-1, word1, word2, dp_arr)
        );
    }
    int minDistance(string word1, string word2) {
        vector<vector<int> > dp_arr(word1.size()+1 , vector<int> (word2.size()+1, -1));
        return DP(word1.length(), word2.length(), word1, word2, dp_arr);
        
    }
};