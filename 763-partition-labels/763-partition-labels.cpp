class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char,pair<int,int>> m;
        vector<pair<int,int>> intervals;
        for (int i=0;i<s.size();i++){
            if(m.count(s[i])) m[s[i]] = {m[s[i]].first,i};
            else m[s[i]] = {i,i};
        }
        
        for(auto i:m) intervals.push_back({i.second});
        sort(intervals.begin(),intervals.end());
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
        for(int i=0;i<ans.size();i++) res[i] = ans[i].second-ans[i].first+1;
        return res;
    }
};