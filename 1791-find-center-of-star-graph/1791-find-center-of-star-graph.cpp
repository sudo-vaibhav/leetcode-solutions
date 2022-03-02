class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        map<unsigned int, unsigned int> degree;
        for(unsigned int i=0;i<2;i++){
            degree[edges[i][0]]++;
            degree[edges[i][1]]++;
        }
        
        for(auto i:degree){
            if(i.second!=1){
                return i.first;
            }
        }
        
        return 0;
    }
};