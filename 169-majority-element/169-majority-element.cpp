class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate;
        unsigned short count=0;
        
        for(int i=0;i<nums.size();i++){
            if(!count){
                candidate = nums[i];
            }
            if(candidate == nums[i]) count++;
            else count--;
        }
        
        return candidate;
    }
};
