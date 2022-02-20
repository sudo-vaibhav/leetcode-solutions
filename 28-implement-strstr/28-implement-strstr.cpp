// O(n) solution \U0001f525
class Solution {
public:
    vector<int> z;
    
    void populateZArray(string s){
        int l = 0,r=0,n = s.size();
        z = vector<int>(n);
        for(int i=1;i<s.size();i++){
            if(i<=r){
                z[i] = min(r-i+1,z[i-l]);
            }
            
            while(i+z[i]<n&&s[z[i]]==s[i+z[i]]){
                z[i]++;
            }
            
            if(i+z[i]-1>r){
                r = i+z[i]-1;
                l = i;
            }
        }
    }
    
    int strStr(string haystack, string needle) {
        string temp = needle+"#"+haystack;
        populateZArray(temp);
        if(needle=="") return 0;
        cout<<temp<<endl;
        
        for(int i=needle.size()+1;i<temp.size();++i){
            if(z[i]==needle.size()){
                return i-needle.size()-1;    
            }
        }
        
        return -1;
    }
};