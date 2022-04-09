class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> m;
        for(auto i:nums){
            m[i]++;
        }
        vector<pair<int,int>> f;
        for(auto i:m){
            f.push_back({i.second,i.first});
        }
        nth_element(f.begin(),f.begin()+f.size()-k,f.end());
        vector<int>ans;
        int n = f.size();
        for(int i=n-1;i>=n-k;i--){
            ans.push_back(f[i].second);
        }
        return ans;
    }
};