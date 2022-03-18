class Solution {
public:
    string smallestSubsequence(string s) {
        string ans = "";
        char a = 'a';
        int n = s.size();
        bool seen[26]={false};
        int highestIdx[26];
        for(int i=0;i<n;i++){
            highestIdx[s[i]-a]= i;
        }
        
        for(int i=0;i<n;i++){
            if(!seen[s[i]-a]){
                while(!ans.empty()&&ans.back()>s[i]&&highestIdx[ans.back()-a]>i){
                    seen[ans.back()-a]=false;
                    ans.pop_back(); 
                }
                ans.push_back(s[i]);
                seen[s[i]-a]=true;
            }
            else continue;
        }
        return ans;
    }
};