class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int n = grid.size(),m=grid[0].size();
        bool visited[n][m];
        memset(visited,false,sizeof(visited));
        int ans = 0;
        for (int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(!visited[i][j]&&grid[i][j]==1){
                    queue<pair<int,int>> q;
                    q.push({i,j});
                    vector<pair<int,int>> deltas={{-1,0},{1,0},{0,1},{0,-1}};
                    visited[i][j]=true;
                    int curAns = 1;
                    while(!q.empty()){
                        auto cur = q.front();q.pop();
                        // visited[cur.first][cur.second]=true;
                        for(auto delt : deltas){
                            int I = cur.first+delt.first;
                            int J = cur.second + delt.second;
                            if(0<=I && I<n && 0<=J && J<m && !visited[I][J] && grid[I][J]==1){
                                visited[I][J] = true;
                                curAns++;
                                q.push({I,J});
                            }
                        }
                    }
                    
                    ans = max(ans,curAns);
                    
                }
            }
        }
        return ans;
    }
};