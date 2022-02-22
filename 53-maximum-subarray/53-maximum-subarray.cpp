class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curSum = nums[0];
        int maxSoFar = nums[0];
        int n = nums.size();
        for(int i=1;i<n;i++){
            if(curSum<0) curSum=0;
            curSum+=nums[i];
            
            maxSoFar = max(maxSoFar,curSum);
        }
        
        return maxSoFar;
    }
};