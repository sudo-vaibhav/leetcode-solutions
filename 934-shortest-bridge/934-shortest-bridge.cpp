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
        return ans;
    }
    
    int shortestBridge(vector<vector<int>>& grid) {
        auto islands = getIslands(grid);
        int m=grid.size(),n=grid[0].size();
        // int ans = INT_MAX;
        queue<pair<int,int>> q;
        for(auto& t:islands[0]){
            // cout<<t[0]<<" "<<t[1]<<"\n";
            q.push({t[0],t[1]});
        }
        set<pair<int,int>> s;
        // cout<<"second island\n";
        for(auto& land:islands[1]){
            s.insert({land[0],land[1]});
        }
        // cout<<"checking set\n";
        // for(auto& e:s){
        //     cout<<e.first<<" "<<e.second<<"\n";
        // }
        int dist = 0;
        // for(auto& row:grid){
        //     for(auto col:row){
        //         cout<<col<<" ";
        //     }
        //     // cout<<"\n";
        // }
        while(!q.empty()){
            int qSize = q.size();
            for(int i=0;i<qSize;i++){
                auto cur = q.front();q.pop();
                // cout<<cur.first<<" "<<cur.second<<"\n";
                for(const auto move:moves){
                    int I=cur.first+move[0],J=cur.second+move[1];
                    
                    if(s.count({I,J})) return dist;
                    if(I>=0 && I<m && J>=0 && J<n && grid[I][J]==0){
                        // cout<<I<<" "<<J<<"\n";
                        grid[I][J]=1;
                        q.push({I,J});
                    }
                }
            }
            dist++;
        }
        return -1;
    }
};