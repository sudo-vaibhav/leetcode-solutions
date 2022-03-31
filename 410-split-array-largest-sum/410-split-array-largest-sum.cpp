class Solution {
public:
    
    int findSubArrayCount(vector<int>& nums,int maxSum){
        int m=1;
        int s=nums[0];
        for(int i=1;i<nums.size();i++){
            if(s+nums[i]>maxSum){
                m++;
                s=nums[i];
            }
            else{
                s+=nums[i];
            }
        }
        return m;
    }
    int splitArray(vector<int>& nums, int m) {
        int lowestMaxSubSum = *max_element(nums.begin(),nums.end());
        int maxMaxSubSum = accumulate(nums.begin(),nums.end(),0);
        int ans = maxMaxSubSum;
        while(lowestMaxSubSum<=maxMaxSubSum){
            int midMaxSubSum = (lowestMaxSubSum+maxMaxSubSum)/2;
            auto suggestedM = findSubArrayCount(nums,midMaxSubSum);
            if(suggestedM<=m){
                ans = min(ans,midMaxSubSum);
                maxMaxSubSum=midMaxSubSum-1;
            }
            else{
                lowestMaxSubSum=midMaxSubSum+1;
            }
        }
        return ans;
    }
};