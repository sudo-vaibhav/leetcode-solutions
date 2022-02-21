class Solution {
public:
    int target;
    int solve(vector<int>& nums,int L, int R){
        int mid = L+(R-L)/2; // 3 
        int val = nums[mid];
        if(val==target) return mid;
        if(L>=R) return -1;
        return max(solve(nums, mid+1,R),solve(nums, L, mid-1));  
    }
    int search(vector<int>& nums, int t) {
        // target 0
        // 2 ,4,5,6,7,    0,1,
        // L      M         R
        target = t;
        int L = 0;
        int R = nums.size()-1; // 6
        
        return solve(nums, L,R);
        
    }
};