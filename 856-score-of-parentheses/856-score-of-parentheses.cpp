// class Solution {
// public:
//     int scoreOfParentheses(string s) {
//         stack<int> scoreAtLevel;
//         scoreAtLevel.push(0); // overall level
//         for(auto c:s){
//             if(c=='('){
//                 scoreAtLevel.push(0);
//             }
//             else{
//                 auto v = scoreAtLevel.top();
//                 scoreAtLevel.pop();
//                 auto newV = scoreAtLevel.top()+max(2*v,1);
//                 scoreAtLevel.pop();
//                 scoreAtLevel.push(newV);
//             }
//         }
        
//         return scoreAtLevel.top();
        
//     }
// };

class Solution {
public:
    int scoreOfParentheses(string s) {
        int ans = 0,outerParenCount=0;
        for(auto i=0;i<s.size();i++){
            auto c = s[i];
            if(c=='('){
                outerParenCount++;
            }
            else{
                outerParenCount--;
                if(s[i-1]=='('){
                    ans += 1<<outerParenCount;
                }
            }
        }
        return ans;
        
    }
};