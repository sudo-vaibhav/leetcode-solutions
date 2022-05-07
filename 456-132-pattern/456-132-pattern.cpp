class Solution {
public:
    bool find132pattern(vector<int>& nums) 
    {
        stack<int>s;
        
        int c=INT_MIN;
        
        for(int i=nums.size()-1;i>=0;i--)
        {
            if(nums[i]<c)
            {
                return true;
            }
            
            while(s.size()!=0 && s.top()<nums[i])
            {
                c=s.top();
                s.pop();
            }
            s.push(nums[i]);
        }
        
        return false;
    }
};