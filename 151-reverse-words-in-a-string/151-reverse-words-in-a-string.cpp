class Solution {
public:
    // stack based implementation (O(n))
    string reverseWords(string s) {
        // remove spaces that are extra
        stack<string> st;
        string temp = "";
        for(auto i=0;i<s.size();i++){
            auto cur = s[i];
            if(cur==' '){
                if(temp.size())
                st.push(temp);
                temp = "";
            }
            else{
                temp+= cur;
            }
        }
        if(temp.size()){
            st.push(temp);
        }
        string ans="";
        while(!st.empty()){
            if(st.top().size())
            ans += st.top();
            st.pop();
            if(!st.empty()){
                ans+=" ";
            }
        }
        cout<<ans;
        return ans;
    }
    
    
};