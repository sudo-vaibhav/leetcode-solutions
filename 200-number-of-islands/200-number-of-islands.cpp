class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<bool>> visited(m,vector<bool>(n,false));
        
        int islandCount = 0;
        
        for(int r=0;r<m;r++){
            for(int c=0;c<n;c++){
                if(grid[r][c]=='1'&&!visited[r][c]){
                    visited[r][c]=1;
                    islandCount++;
                     // now we do bfs and mark nearby connected parts
                    queue<pair<int,int>> q;
                    q.push({r,c});

                    while(!q.empty()){
                        int temp = q.size();
                        while(temp--){
                            auto cur = q.front();
                            q.pop();
                            vector<pair<int,int>> moves = {{-1,0},{1,0},{0,1},{0,-1}};
                            for(auto move:moves){
                                auto R = cur.first+move.first;
                                auto C = cur.second+move.second;
                                if(R>=0&&R<m && C>=0 && C<n){
                                    if(grid[R][C]=='1'&&!visited[R][C]){
                                        visited[R][C] = 1;    
                                        q.push({R,C});
                                    }
                                }
                            }
                        }

                    }
                    
                   
                }
            }
        }
        
        return islandCount;
    }
};