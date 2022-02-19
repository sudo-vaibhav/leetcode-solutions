class Solution {
public:
    int myAtoi(string s) {
        // stack<char> st;
        int n = s.size();
        int pointer = 0;
        for(;pointer<n;pointer++){
            auto val = s[pointer];
            if(val!=' '){
                break;
            }
        }
        
        long long ans=0;
        
        bool positive = (pointer<n) ? (s[pointer]=='-'?false:true) : true;
        
        cout<<"positive: "<<positive<<endl;
        if(s[pointer]!='-'&&s[pointer]!='+'&&!(s[pointer]>='0'&&s[pointer]<='9')){
            cout<<"violated valid integer"<<endl;
            return 0;
        }
        if(s[pointer]=='-'||s[pointer]=='+')pointer++;
        while(true){
            if(s[pointer]>='0'&&s[pointer]<='9'&&pointer<n){
                if(ans<INT_MAX)
                ans = ans*10 + (s[pointer]-'0');
                pointer++; 
                continue;
            }
            if(pointer>=n) {
                cout<<"reached end of string"<<endl;
                break;
            }
            else{
                break;
            }
        }
        
        if(positive){
            if(ans>(pow(2,31)-1)){
                return INT_MAX;
            }
            else{
                return ans;
            }
        }
        else{
            if(ans>(pow(2,31))){
                return INT_MIN;
            }
            else{
                return -1*ans;
            }
        }
    }
};