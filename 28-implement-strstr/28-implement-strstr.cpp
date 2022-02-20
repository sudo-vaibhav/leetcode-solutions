// O(n) solution \U0001f525
class Solution {
public:
    vector<int> z;
    
    void populateZArray(string s){
        // initialise l, r and n
        int l = 0,r=0,n = s.size();
        
        // initialise z vector
        z = vector<int>(n);
        
        // from index 1 to n-1 , find length of prefix match found at position i
        for(int i=1;i<s.size();i++){
            
            // take boost if you are in the l to r zone
            if(i<=r){
                z[i] = min(r-i+1,z[i-l]);
            }
            // increment z[i] if current matches happen
            while(i+z[i]<n&&s[z[i]]==s[i+z[i]]){
                z[i]++;
            }
            
            // reconfigure l and r if you have exceeded current boundary
            if(i+z[i]-1>r){
                r = i+z[i]-1;
                l = i;
            }
            
        }
        
    }
    
    int strStr(string haystack, string needle) {
        if(needle=="") return 0;
        
        // add a delimiter between needle and haystack
        // this delimiter should not be part of character space of 
        // given input
        string temp = needle+"#"+haystack;
        
        // call z-function
        populateZArray(temp);
        
        // inside haystack find those places whose z value 
        // is equal to length of needle
        for(int i=needle.size()+1;i<temp.size();++i){
            if(z[i]==needle.size()){
                return i-needle.size()-1;    
            }
        }
        
        // if no match return -1
        return -1;
    }
};