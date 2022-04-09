class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> m; // create a frequency map
        for(auto i:nums) m[i]++; // populate the map
        vector<pair<int,int>> f; // declare a vector and have frequency as sort key
        for(auto i:m) f.push_back({i.second,i.first}); // populate the freq vector
        nth_element(f.begin(),f.begin()+f.size()-k,f.end()); // qk select to have k largest numbers in place (but not sorted)
        vector<int>ans; // answer vector
        int n = f.size(); // n
        for(int i=n-1;i>=n-k;i--) ans.push_back(f[i].second); // get k most frequent in answer
        return ans; // return ans
    }
};