// struct comp{

//     bool operator()
// };
class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(),intervals.end(),[](vector<int> a , vector<int> b){
        if(a[0]==b[0]){
            return a[1]>b[1];   
        }
        else{
            return a[0]<b[0];
        }
    });
        auto prev = intervals[0];
        auto count=0;
        for(auto i=1;i<intervals.size();i++){
            if(prev[0]<=intervals[i][0]&& prev[1]>=intervals[i][1]){
                count++;
            }
            else{
                prev = intervals[i];
            }
        }
        
        return intervals.size()-count;
    }
};