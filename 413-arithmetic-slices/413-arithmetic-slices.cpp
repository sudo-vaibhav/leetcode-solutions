class Solution {
public:
    int getCounts(int simCount){
        return ((simCount-1)*simCount)/2;
    }
    
    int numberOfArithmeticSlices(vector<int>& nums) {
        unsigned int simCount = 1;
        unsigned int ans = 0;
        for(auto i=2;i<nums.size();i++){
            if(nums[i]-nums[i-1]==nums[i-1]-nums[i-2]){
                simCount++;
            }
            else{
                ans+= getCounts(simCount);
                simCount = 1;
            }
        }
        ans+= getCounts(simCount);
        return ans;
    }
};