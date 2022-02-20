class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        // sort on basis of start of intervals
        sort(intervals.begin(),intervals.end(),[](vector<int> a,vector<int> b){
            return a[0]<b[0];
        });
        
        vector<vector<int>> ans;
        
        // seed the prev with first value of newly sorted intervals
        vector<int> prev = intervals[0];
        
        for(auto i=1;i<intervals.size();i++){
            auto cur = intervals[i];
            
            if(prev[1]<cur[0]){
                // no overlap
                ans.push_back(prev);
                prev = cur;
            }
            else{
                // overlap exists
                
                // pick best possible lower value
                prev[0] = min(prev[0],cur[0]);
                
                // pick best possible upper value
                prev[1] = max(prev[1],cur[1]);
            }
        }
        
        
        // there will always be one remainder ans left in prev, add that also
        ans.push_back(prev);
        
        
        // finally return answer
        return ans;
        
    }
};