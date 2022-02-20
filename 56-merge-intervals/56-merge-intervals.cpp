class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(),intervals.end(),[](vector<int> a,vector<int> b){
            return a[0]<b[0];
        });
        
        vector<vector<int>> ans;
        vector<int> prev = intervals[0];
        
        for(auto i=1;i<intervals.size();i++){
            auto cur = intervals[i];
            
            if(prev[1]<cur[0]){
                // no overlap
                ans.push_back(prev);
                prev = cur;
            }
            else{
                prev[0] = min(prev[0],cur[0]);
                prev[1] = max(prev[1],cur[1]);
            }
        }
        
        ans.push_back(prev);
        
        return ans;
        
    }
};