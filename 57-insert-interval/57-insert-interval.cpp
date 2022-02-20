// O(nlogn) solution as we are still sorting in end, which can be avoided
// class Solution {
// public:
//     vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        
//         vector<int> goalInterval = newInterval;
//         vector<vector<int>> ans;
        
//         for(auto i:intervals){
//             // if no overlap
//             if(i[0]>newInterval[1]||newInterval[0]>i[1]){
//                 // no need for adjusting goal
//                 // also because there is no overlap, we can push this straight to
//                 // answer
//                 ans.push_back(i);
//             }
//             else{
//                 goalInterval[0] = min(i[0],goalInterval[0]);
//                 goalInterval[1] = max(i[1],goalInterval[1]);
//             }
//         }
        
//         // finally insert goal interval to ans
//         ans.push_back(goalInterval);
        
//         // sort array again so that goal interval goes in its place
        
//         sort(ans.begin(),ans.end(),[](vector<int> a, vector<int> b){
//             return a[0]<b[0];
//         });
     
//         return ans;
//     }
// };


// O(n) approach, without sorting
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        
        vector<int> goalInterval = newInterval;
        vector<vector<int>> ans;
        bool done = false;
        for(auto i:intervals){
            // if no overlap
            if(newInterval[0]>i[1]){
                // no need for adjusting goal
                // also because there is no overlap, we can push this straight to
                // answer
                ans.push_back(i);
            }
            else if(i[0]>newInterval[1]){
                // if not inserted goalInterval yet, then insert
                if(!done){
                    done = true;
                    ans.push_back(goalInterval);
                }
                ans.push_back(i);
            }
            else {
                goalInterval[0] = min(i[0],goalInterval[0]);
                goalInterval[1] = max(i[1],goalInterval[1]);
            }
        }
        
        if(!done) ans.push_back(goalInterval);
        return ans;
    }
};