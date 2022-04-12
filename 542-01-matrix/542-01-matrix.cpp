class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        queue<vector<int>> q;
        int m=mat.size(),n=mat[0].size();
        vector<vector<int>> dist(m,vector<int>(n,INT_MAX));
        vector<vector<int>> moves = {{-1,0},{1,0},{0,1},{0,-1}};
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(mat[i][j]==0){
                    dist[i][j]=0;
                    q.push({i,j});
                }
            }
        }
        while(!q.empty()){
            auto cur = q.front();q.pop();
            for(auto& move:moves){
                auto I = cur[0]+move[0];
                auto J = cur[1]+move[1];
                if(I<m && I>=0 && J<n && J>=0 && mat[I][J]==1 && dist[I][J]>1+dist[cur[0]][cur[1]]){
                    dist[I][J] = 1+dist[cur[0]][cur[1]];
                    q.push({I,J});
                }
            }
        }
        return dist;
        
        
    }
};