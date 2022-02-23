class Solution {
public:
    void solve(int idx, vector<int>& candidates, vector<int>& picks,vector<vector<int>>& ans,int target){
        int n = candidates.size();
        if(target==0) {
            ans.push_back(picks);
            return;
        }
        if(idx==n) return;
        
        for(int i=idx;i<n;i++){
            if(candidates[i]>target) break;
            if(i>idx&&candidates[i]==candidates[i-1]) continue;
            picks.push_back(candidates[i]);
            solve(i+1,candidates,picks,ans,target-candidates[i]);
            picks.pop_back();
        }
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> temp;
        sort(candidates.begin(),candidates.end());
        solve(0,candidates,temp,ans,target);
        return ans;
    }
};