class Solution {
public:
//     manhattan distance
    int manDist(const vector<int>& l1,const vector<int>& l2){
        return abs(l1[0]-l2[0])+abs(l1[1]-l2[1]);
    }
    const vector<vector<int>> moves=  {{-1,0},{1,0},{0,1},{0,-1}};
    vector<vector<vector<int>>> getIslands(const vector<vector<int>>& grid){
        int m=grid.size(),n=grid[0].size();
        vector<vector<bool>> visited(m,vector<bool>(n,false));
        vector<vector<vector<int>>> ans;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if (!visited[i][j] && grid[i][j]==1){
                    queue<vector<int>> q;
                    q.push({i,j});
                    visited[i][j]=true;
                    vector<vector<int>> temp;
                    while(!q.empty()){
                        auto cur = q.front();q.pop();
                        temp.push_back(cur);
                        for(auto& move:moves){
                            int I=cur[0]+move[0],J=cur[1]+move[1];
                            if(I>=0 && I<m && J>=0 && J<n && !visited[I][J] && grid[I][J]==1){
                                visited[I][J]=true;
                                q.push({I,J});
                            }
                        }
                    }
                    ans.push_back(temp);
                }
                
            }
        }
        // cout<<ans.size();
        return ans;
    }
    
    int shortestBridge(vector<vector<int>>& grid) {
        auto islands = getIslands(grid);
        int ans = INT_MAX;
        for(auto& land : islands[0]){
            for(auto& land2:islands[1]){
                ans = min(ans,manDist(land,land2));
            }
        }
        
        return ans-1;
    }
};