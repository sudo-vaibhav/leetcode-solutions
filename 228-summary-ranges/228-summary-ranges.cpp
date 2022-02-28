class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        if(nums.size()==0) return {};
        if(nums.size()==1) return {to_string(nums[0])};
        int intervalTarget = nums[0];
        int intervalStart = nums[0];
        int count=0;
        int n = nums.size();
        vector<string> ans;
        for(int i=0;i<n;i++){
            auto cur = nums[i];
            if(i<n&&abs((long)intervalTarget-(long)cur)<=1){
                intervalTarget = cur;
                count++;
            }
            else{
                if(count>1){
                    ans.push_back(to_string(intervalStart) +"->"+to_string(nums[i-1]));
                    
                }
                else{
                    ans.push_back(to_string(intervalStart));
                }
                intervalStart = cur;
                intervalTarget = cur;
                count=1;
                
            }
        }
        if(count>1){
                    ans.push_back(to_string(intervalStart) +"->"+to_string(nums[n-1]));
                    
                }
                else{
                    ans.push_back(to_string(intervalStart));
                }
        return ans;
    }
};