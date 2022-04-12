class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        int m= grid.size(),n=grid[0].size();
        vector<vector<int>> dist(m,vector<int>(n,INT_MAX));
        vector<vector<int>> moves = {{-1,0},{1,0},{0,1},{0,-1}};
        int land = 1,water=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==land){
                    queue<vector<int>> q;
                    dist[i][j]=0;
                    q.push({i,j});
                    int steps = 0;
                    while(!q.empty()){
                        int s = q.size();
                        steps++;
                        for(int i=0;i<s;i++){
                            auto cur = q.front();q.pop();
                            for(auto& move:moves){
                                auto I = cur[0]+move[0];
                                auto J = cur[1]+move[1];
                                if(I>=0 && I<m && J>=0 && J<n && grid[I][J]==water && steps<dist[I][J]){
                                    dist[I][J]=steps;
                                    q.push({I,J});
                                }
                            }
                        }
                    }
                }
            }
        }
        
        int ans = INT_MIN;
        for(auto& row:dist){
            for(auto& v:row){
                if(v>0){
                    ans = max(ans,v);
                }    
            }
        }
        return (ans==INT_MIN||ans==INT_MAX)?-1:ans;
    }
};