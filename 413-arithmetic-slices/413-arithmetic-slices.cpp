class Solution {
public:
    int getCounts(int simCount){
        const auto numOfElems = simCount+1;
        return ((numOfElems-2)*(numOfElems-1))/2;
    }
    
    int numberOfArithmeticSlices(vector<int>& nums) {
        int simCount = 1;
        int ans = 0;
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