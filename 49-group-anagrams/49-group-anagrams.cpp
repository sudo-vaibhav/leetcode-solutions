class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map <string, vector<string>> m;
        
        for(auto i=0;i<strs.size();i++){
            auto temp = strs[i];
            sort(temp.begin(),temp.end());
            m[temp].push_back(strs[i]);
        }
        vector<vector<string>>ans;
        for(auto i:m){
            ans.push_back(i.second);
        }
        
        return ans;
    }
};