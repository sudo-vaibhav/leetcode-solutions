class Solution {
public:
    int solve(vector<int>& nums){
        int previ = nums[0],prev2i = 0;
        
        for(int i=1;i<nums.size();i++){
            auto ans = max(previ,prev2i+nums[i]);
            prev2i = previ;
            previ = ans;
        }
        
        return previ;
    }
    
    int rob(vector<int>& nums) {
        
        auto n = nums.size();
        if (n==1) return nums[0];
        auto lastElem = nums[n-1];
        nums.pop_back();
        auto firstElem = nums[0];
        auto withoutEnd = solve(nums);
        nums.push_back(lastElem);
        nums.erase(nums.begin());
        auto withoutBegin = solve(nums);
        nums.insert(nums.begin(),firstElem);
        return max(withoutEnd,withoutBegin);
    }
};