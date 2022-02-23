class Solution {
public:
    void solve(vector<int>& nums, vector<multiset<int>>&ans){
        int n = nums.size();
        // if(idx==n){
        
        // }
        // else{
        //     for(int i=idx;i<n;i++){
        //         swap(nums[i],nums[idx]);
        //         solve(i+1,nums,ans);
        //         swap(nums[i],nums[idx]);
        //     }
        // }
        for(int i=0;i<pow(2,n);i++){
            auto temp = i;
            multiset<int> curSubset;
            int j=0;
            while(temp){
                auto toTake = temp&1;
                temp>>=1;
                if(toTake) curSubset.insert(nums[j]);      
                j++;
            }
            bool dup = false;
            for(auto i:ans){
                if (curSubset==i) dup=true;
            }
            if (!dup){
                ans.push_back(curSubset);
            }
        }
    }
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<multiset<int>> ans;
        solve(nums,ans);
        vector<vector<int>> res;
        for(auto i:ans){
            res.push_back(vector<int>(i.begin(),i.end()));
        }
        return res;
    }
};