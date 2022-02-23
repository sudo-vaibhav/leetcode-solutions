class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size(); // 2, [2,2]
        vector<int> ans; // empty
        for(int i=0;i<n;i++){ 
            int val = abs(nums[i]); // 2
            if(nums[val-1]>0){
                nums[val-1]*=-1; // [2,-2]
            }
            else{
                ans.push_back(val); //
            }
        }
        
        for(int i=0;i<n;i++){
            if(nums[i]>0){
                ans.push_back(i+1);
            }
        }
        
        return ans;
    }
};