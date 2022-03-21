// class Solution {
// public:
//     void sortColors(vector<int>& nums) {
//         sort(nums.begin(),nums.end());
//     }
// };

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int lo = 0,hi = nums.size()-1,mid = 0;
        while(mid<=hi){
            switch(nums[mid]){
                case 0:
                    swap(nums[mid++],nums[lo++]);
                    break;
                case 1:
                    mid++;
                    break;
                default:
                    swap(nums[mid],nums[hi--]);
                    
            }
        }
    }
};