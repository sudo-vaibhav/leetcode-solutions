class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if(grid[0][0]==1) return -1;
        queue<vector<int>> q;
        int m = grid.size(),n=grid[0].size();
        bool found = false;
        q.push({0,0});
        int dist = 0;
        vector<vector<int>> moves = {
            {1,0},{-1,0},{0,1},{0,-1},
            {-1,-1},{1,1},{1,-1},{-1,1}
        };
        grid[0][0]=2;
        while(!q.empty()){
            
            auto s = q.size();
            for(int i=0;i<s;i++){
                auto cur = q.front();q.pop();
                
                if(cur[0]==m-1 && cur[1]==n-1) return dist+1;
                for(auto& move : moves){
                    auto I = move[0]+cur[0];
                    auto J = move[1]+cur[1];
                    if(I>=0 && I<m && J>=0 and J<n && grid[I][J]==0){
                        grid[I][J]=2;
                        q.push({I,J});
                    }
                }
            }
            
            dist++;
            
        }
        
        return -1;
    }
};