// class Solution:
//     def minCut(self, s: str) -> int:
//         n = len(s)
//         @cache
//         def isPalindrome(i,j):
//             while i<j-1:
//                 if s[i]!=s[j-1]: return False
//                 i+=1
//                 j-=1
//             return True
//         @cache
//         def solve(i,j):
//             if isPalindrome(i,j):
//                 return 0
//             else:
//                 ans = 2000
//                 for k in range(i+1,j):
//                     if isPalindrome(i,k):
//                         tempans = 1+solve(k,j)
//                         if tempans < ans:
//                             ans = tempans
//                 return ans
//         return solve(0,len(s))

class Solution {
public:
     int dp[2001][2001];
    bool isPalindrome(int i,int j,string& s){
        while(i<j){
            if(s[i]!=s[j]) return false;
            i++;
            j--;
        }
        return true;
    }
    
    int solve(int i, int j, string& s){
        if(dp[i][j]!=-1) return dp[i][j];
        if(isPalindrome(i,j,s)) return dp[i][j]=0;
        else{
            auto ans = 2500;
            for(int k=i;k<j;k++){
                if(isPalindrome(i,k,s)){
                    ans = min(ans,1+solve(k+1,j,s));
                }
            }
            return dp[i][j]=ans;
        }
    }
    
    int minCut(string s) {
        auto n = s.size();
        memset(dp,-1,sizeof(dp));
        return solve(0,n-1,s);
        // return dp[0][n-1];
    }
};