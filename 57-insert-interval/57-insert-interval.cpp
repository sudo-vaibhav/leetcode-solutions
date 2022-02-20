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
        
        for(auto i:intervals){
            // if no overlap
            if(i[0]>newInterval[1]||newInterval[0]>i[1]){
                // no need for adjusting goal
                // also because there is no overlap, we can push this straight to
                // answer
                ans.push_back(i);
            }
            else{
                goalInterval[0] = min(i[0],goalInterval[0]);
                goalInterval[1] = max(i[1],goalInterval[1]);
            }
        }
        
        // finally insert goal interval to ans
        ans.push_back(goalInterval);
        
        // find first time where goalInterval[0] is exceeded
        int exceed_pos = 0;
        for(exceed_pos=0;exceed_pos<ans.size();++exceed_pos){
            auto cur = ans[exceed_pos];
            // cout<<"cur: "<<cur[0]<<endl;
            if(cur[0]>=goalInterval[0]){
                break;
            }
        }
        
        // now starting from exceed pos to end-1 , shift all elements to right
        // if(ans.size())
        // cout<<"size:"<<ans.size()<<endl;
        // cout<<"exceed pos:"<<exceed_pos<<endl;
        for(int i = ans.size()-1;i>exceed_pos;--i){
            ans[i] = ans[i-1];
        }
//         // finally put goal interval in its place
        ans[exceed_pos] = goalInterval;
        
        return ans;
    }
};