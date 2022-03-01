class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        vector<int> temp;
        for(auto i:matrix){
            for (auto j:i){
                temp.push_back(j);
            }
        }
        
        sort(temp.begin(),temp.end());
        return temp[k-1];
    }
};