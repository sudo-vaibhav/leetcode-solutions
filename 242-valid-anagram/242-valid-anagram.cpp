class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> charUsage;
        for(auto i:s){
            charUsage[i]++;
        }
        
        for(auto i:t){
            charUsage[i]--;
            if(charUsage[i]==0){
                charUsage.erase(i);
            }
        }
        
        return charUsage.size()==0;
    }
};