class Solution {
public:
    
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> s;
        int n = pushed.size(),pushIdx=0,poppedIdx=0;
        
        while(true){
            if(poppedIdx==n && s.empty()) return true;
            if(s.empty()||s.top()!=popped[poppedIdx]){
                if(pushIdx==n){
                    return false;
                }
                else{
                    s.push(pushed[pushIdx++]);
                }
            }
            else{
                s.pop();
                poppedIdx++;
            }
        }
        return false;
    }
};