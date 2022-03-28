class Solution {
public:
    int closedIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<bool>> visited(m,vector<bool>(n,false));
        
        int islandCount = 0;
        
        for(int r=1;r<m-1;r++){
            for(int c=1;c<n-1;c++){
                if(grid[r][c]==0&&!visited[r][c]){
                    visited[r][c]=1;
                    
                     // now we do bfs and mark nearby connected parts
                    queue<pair<int,int>> q;
                    q.push({r,c});
                    bool problem = false;
                    while(!q.empty()){
                        auto cur = q.front();q.pop();
                        vector<pair<int,int>> moves = {{-1,0},{1,0},{0,1},{0,-1}};
                        for(auto move:moves){
                            auto R = cur.first+move.first;
                            auto C = cur.second+move.second;
                            if(R>=0&&R<m && C>=0 && C<n && grid[R][C]==0&&!visited[R][C]){
                                if(R==0 || R==m-1 || C==n-1 || C==0) {
                                    problem = true;
                                }
                                visited[R][C] = 1;    
                                q.push({R,C});
                            }
                        }
                    }
                    
                    if(!problem){
                        islandCount++;
                    }
                    // islandCount+= !problem;
                }
            }
        }
        
        return islandCount;
    }
};