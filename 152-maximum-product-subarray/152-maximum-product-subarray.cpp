class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int minimum=nums[0],maximum=nums[0],ans=nums[0];
        for(int i=1;i<nums.size();i++){
            if(nums[i]<0){
               swap(maximum,minimum);
            }
            
            maximum = max(nums[i],maximum*nums[i]);
            minimum = min(nums[i],minimum*nums[i]);
            ans =  max(ans,maximum);
        }
        
        return ans;
    }
};