class Solution {
public:
    
    stack<int> s;
    vector<int> prevGreater(vector<int>& nums){
        const int n = nums.size();
        vector<int> ans(n);
        for(int i=0;i<n;i++){
            while(!s.empty()&&nums[s.top()]<=nums[i]){
                s.pop();
            }
            if(s.empty()){
                ans[i] = -1;
                s.push(i);
            }
            else{
                auto temp = s.top();
                int idx = temp;
                while(!s.empty()&&nums[s.top()]>=nums[i]){
                    idx = s.top();
                    s.pop();
                }
                ans[i] = idx;
                s.push(idx);
            }
        } 
        
        return ans;
    }
    
    
    vector<int> nextGreater(vector<int>& nums){
        const int n = nums.size();
        vector<int> ans(n);
        
        for(int i=n-1;i>=0;i--){
            while(!s.empty()&&nums[s.top()]<=nums[i]){
                s.pop();
            }
            if(s.empty()){
                ans[i] = -1;
                s.push(i);
            }
            else{
                auto temp = s.top();
                int idx = temp;
                while(!s.empty()&&nums[s.top()]>=nums[i]){
                    idx = s.top();
                    s.pop();
                }
                ans[i] = idx;
                s.push(idx);
            }
        } 
        
        return ans;
    }
    
    int trap(vector<int>& nums) {
        int n = nums.size();
        auto prev = prevGreater(nums);
        s= stack<int>();
        auto next = nextGreater(nums);
        int ans = 0;
        
        // p(prev,nums);
        // p(next,nums);
        
        // cout<<"Max Possibles:"<<endl;
        for(int i=0;i<n;i++){
            auto temp = min(
                prev[i]!=-1 ? nums[prev[i]] : 0,
                next[i]!=-1 ? nums[next[i]] : 0
            );
            // cout<<temp-nums[i]<<"\t";
            ans += max(temp-nums[i],0);
        }
        
        return ans;
    }
};