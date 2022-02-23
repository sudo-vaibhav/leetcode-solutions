// APPROACH 1 using multiset
// class Solution {
// public:
//     void solve(vector<int>& nums, vector<multiset<int>>&ans){
//         int n = nums.size();
//         for(int i=0;i<pow(2,n);i++){
//             auto temp = i;
//             multiset<int> curSubset;
//             int j=0;
//             while(temp){
//                 auto toTake = temp&1;
//                 temp>>=1;
//                 if(toTake) curSubset.insert(nums[j]);      
//                 j++;
//             }
//             bool dup = false;
//             for(auto i:ans){
//                 if (curSubset==i) dup=true;
//             }
//             if (!dup){
//                 ans.push_back(curSubset);
//             }
//         }
//     }
    
//     vector<vector<int>> subsetsWithDup(vector<int>& nums) {
//         vector<multiset<int>> ans;
//         solve(nums,ans);
//         vector<vector<int>> res;
//         for(auto i:ans){
//             res.push_back(vector<int>(i.begin(),i.end()));
//         }
//         return res;
//     }
// };


// APPROACH 2
class Solution{
    void solve(int idx, vector<int>& nums,vector<int>& ans,vector<vector<int>>& res){
        // first insert whatever is already there, coz its a valid subset
        res.push_back(ans);
        int n = nums.size();
        if(idx==n) return;
        for(int i=idx;i<n;i++){
            if(i!=idx&&nums[i]==nums[i-1]) continue;
            else{
                ans.push_back(nums[i]);
                solve(i+1,nums,ans,res);
                ans.pop_back();
            }
        }
    }
    public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<int> ans;
        vector<vector<int>> res;
        solve(0,nums,ans,res);
        return res;
    }
};