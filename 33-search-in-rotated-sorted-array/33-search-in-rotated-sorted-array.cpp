class Solution {
public:
    int solve(vector<int>& nums,int& target, int L, int R){
        int mid = L+(R-L)/2;
        int val = nums[mid];
        if(val==target) return mid;
        if(L>=R) return -1;
        return max(solve(nums,target, mid+1,R),solve(nums,target, L, mid-1));  
    }
    int search(vector<int>& nums, int target) {
        return solve(nums, target, 0, nums.size()-1);
    }
};