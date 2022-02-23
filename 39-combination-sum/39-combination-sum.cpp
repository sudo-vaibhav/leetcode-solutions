class Solution {
public:
    void solve(int idx,vector<int>& candidates,vector<int>& combination,int target,vector<vector<int>>&ans,int sumSoFar){
        int n = candidates.size();
        
        if(idx==n){
            if(sumSoFar==target) ans.push_back(combination);
        }
        else if(target>=sumSoFar){
            solve(idx+1,candidates,combination,target,ans,sumSoFar);
            combination.push_back(candidates[idx]);
            solve(idx,candidates,combination,target,ans,sumSoFar+candidates[idx]);
            combination.pop_back();
        }
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> combination;
        solve(0,candidates,combination,target,ans,0);
        return ans;
    }
};