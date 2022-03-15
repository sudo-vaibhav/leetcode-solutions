class Solution {
public:
    string minRemoveToMakeValid(string s) {
        stack<int> opening;
        bool allowed[s.size()];
        string ans = "";
        memset(allowed,false,sizeof(allowed));
        
        for (int i=0;i<s.size();i++){
            auto val = s[i];
            if(val=='('){
                opening.push(i);
            }
            else if(val==')'){
                if(!opening.empty()){
                    auto temp = opening.top();
                    allowed[temp] = true;
                    allowed[i] = true;
                    opening.pop();
                }
            }
            else{
                allowed[i]= true;
            }
        }
        
        for(int i=0;i<s.size();i++){
            if(allowed[i]){
                ans+= string(1,s[i]);
            }
        }
        return ans;
    }
};