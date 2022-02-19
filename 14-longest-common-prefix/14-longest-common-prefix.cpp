class Solution {
public:
    bool checkAllEqual(vector<string>& strs,int idx){
        auto reference = strs[0][idx];
        for(auto s:strs){
            if(s[idx]!=reference) return false;
        }
        return true;
    }
    
    string longestCommonPrefix(vector<string>& strs) {
        string ans="";
        unsigned long minimum_length=INT_MAX;
        for(auto i : strs){
            minimum_length = min(minimum_length,i.size());
        }
        auto length=0;
        for(;length<minimum_length;length++){
            if(!checkAllEqual(strs,length)){
                break;
            }
            else{
                ans+=strs[0][length];
            }
        }
        
        return ans;
    }
};