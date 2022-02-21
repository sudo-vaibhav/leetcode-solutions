// O(logn) time and O(logn) space solution (due to recursive stack)
// class Solution {
// public:
//     int solve(vector<int>& nums,int& target, int L, int R){
//         int mid = L+(R-L)/2;
//         int val = nums[mid];
//         if(val==target) return mid;
//         if(L>=R) return -1;
//         return max(solve(nums,target, mid+1,R),solve(nums,target, L, mid-1));  
//     }
//     int search(vector<int>& nums, int target) {
//         return solve(nums, target, 0, nums.size()-1);
//     }
// };

// O(logn) time and O(1) space solution
class Solution{
  public:
    int search(vector<int>& nums, int target){
        int L = 0, R = nums.size()-1;
        while(L<=R){
            
            int mid = L+(R-L)/2;
            int val = nums[mid];
            
            if(val==target) return mid;
            
            if(nums[L]<=nums[mid]){
                // sorted subarray
                if(nums[L]<=target&&target<=val){
                    R = mid-1;
                }
                else{
                    L = mid+1;
                }
            }
            else{
                if(nums[mid]<=target&&target<=nums[R]){
                    L = mid+1;
                }
                else{
                    R = mid-1;
                }
            }
            
        }
        return -1;
    }
};