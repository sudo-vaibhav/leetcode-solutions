    // logic based approach

// class Solution {
// public:
    //     int myAtoi(string s) {
//         // stack<char> st;
//         int n = s.size();
//         int pointer = 0;
//         for(;pointer<n;pointer++){
//             auto val = s[pointer];
//             if(val!=' '){
//                 break;
//             }
//         }
        
//         long long ans=0;
        
//         bool positive = (pointer<n) ? (s[pointer]=='-'?false:true) : true;
        
//         cout<<"positive: "<<positive<<endl;
//         if(s[pointer]!='-'&&s[pointer]!='+'&&!(s[pointer]>='0'&&s[pointer]<='9')){
//             cout<<"violated valid integer"<<endl;
//             return 0;
//         }
//         if(s[pointer]=='-'||s[pointer]=='+')pointer++;
//         while(true){
//             if(s[pointer]>='0'&&s[pointer]<='9'&&pointer<n){
//                 if(ans<INT_MAX)
//                 ans = ans*10 + (s[pointer]-'0');
//                 pointer++; 
//                 continue;
//             }
//             if(pointer>=n) {
//                 cout<<"reached end of string"<<endl;
//                 break;
//             }
//             else{
//                 break;
//             }
//         }
        
//         if(positive){
//             if(ans>(pow(2,31)-1)){
//                 return INT_MAX;
//             }
//             else{
//                 return ans;
//             }
//         }
//         else{
//             if(ans>(pow(2,31))){
//                 return INT_MIN;
//             }
//             else{
//                 return -1*ans;
//             }
//         }
//     }
// };

/*
q0 -> initial state and state where initial whitespaces are to be removed
q1 -> position after which digits will start
q2 -> all digits are processed here
qd -> dead state, processing ends here.
*/
enum State {q0,q1,q2,qd};

class StateMachine{
    State currentState;
    int result ,sign;
    void toStateQ1(char& ch){
        if(ch=='+'){
            sign = 1;
        }
        else{
            sign = -1;
        }
        currentState = q1;
    }
    
    void toStateQ2(int num){
        currentState = q2;
        if((result>INT_MAX/10)||(result==INT_MAX/10&&num>INT_MAX%10)){
            if(sign==1){
                sign = 1;
                result = INT_MAX;
            }
            else{
                sign = 1;
                result = INT_MIN;
            }
            
            toStateQd();
            
        }
        else{
            result = result*10+num;
        }
    }
    
    void toStateQd(){
        currentState = qd;
    }
    
    public:
    
    StateMachine(){
        currentState = q0;
        result = 0;
        sign = 1;
    }
    
    void transition(char& ch){
        if(currentState == q0){
            if(ch==' '){
                // stay here itself
                return;
            }
            else if(ch=='-'||ch=='+'){
                toStateQ1(ch);
            }
            else if(isdigit(ch)){
                toStateQ2(ch-'0');
            }
            else{
                toStateQd();
            }
        }
        else if(currentState==q1||currentState==q2){
            if(isdigit(ch)){
                toStateQ2(ch-'0');
            }
            else{
                toStateQd();
            }
        }
        // we dont't expect to receive a current state of qd here
    }
    
    int getInteger(){
        return result*sign;
    }
    
    State getState(){
        return currentState;
    }
    
    
    
};
class Solution{
    public:
    int myAtoi(string s){
        StateMachine M;
        for(int i=0;i<s.size()&&M.getState()!=qd;++i){
            M.transition(s[i]);
        }
        
        return M.getInteger();
    }
};