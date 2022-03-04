class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<int> inDegrees(n,0);
        for (auto edge:edges){
            inDegrees[edge[1]]++;
        }
        vector<int> ans;
        
        for(auto i=0;i<n;i++){
            if(inDegrees[i]==0){
                ans.push_back(i);
            }
        }
        
        return ans;
    }
};