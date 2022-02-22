class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int v1 = nums[n-1]*nums[n-2]*nums[n-3];
        int v2 = nums[n-1]*nums[0]*nums[1];
        
        return max(v1,v2);
    }
};