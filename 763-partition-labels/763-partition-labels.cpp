class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char,pair<int,int>> m;
        int t = 0;
        for (auto i:s){
            if(m.count(i)){
                m[i] = {m[i].first,t};
            }
            else{
                m[i] = {t,t};
            }
            t++;
        }
        
        vector<pair<int,int>> intervals;
        for(auto i:m){
            intervals.push_back({i.second});
        }
        
        sort(intervals.begin(),intervals.end(),[](pair<int,int> i1,pair<int,int> i2){
            // if(i1.first!=i2.first){
                return i1.first<i2.first;
            // }
            // else{
                // return i1.second<i2.second;
            // }
        });
        vector<pair<int,int>> ans;
        pair<int,int> prev = intervals[0];
        for(int i=1;i<intervals.size();i++){
            auto cur = intervals[i];
            if(cur.first<prev.second){
                prev = {min(prev.first,cur.first),max(prev.second,cur.second)};
            }
            else{
                ans.push_back(prev);
                prev = cur;
            }
        }
        
        // also account for prev
        ans.push_back(prev);
        vector<int> res = vector<int>(ans.size()); 
        for(int i=0;i<ans.size();i++){
            res[i] = ans[i].second-ans[i].first+1;
        }
        return res;
    }
};