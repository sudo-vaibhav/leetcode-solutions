// class Solution {
// public:
//     void nextPermutation(vector<int>& nums) {
//         next_permutation(nums.begin(),nums.end());
//     }
// };

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int temp = INT_MAX;
        for(int i=n-2;i>=0;i--){
            if(nums[i]<nums[i+1]){
                temp = i;
                break;
            }
        }
        
        if(temp==INT_MAX){
            reverse(nums.begin(),nums.end());
        }
        else{
            auto v = nums[temp];
            int i=n-1;
            for(;i>temp;i--){
                if(nums[i]>v){
                    swap(nums[temp],nums[i]);
                    break;
                }
            }
            
            reverse(nums.begin()+temp+1,nums.end());
        }
    }
};