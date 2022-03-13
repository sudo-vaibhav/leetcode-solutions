enum Orange{
    none,
    fresh,
    rotten
};

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size(),n= grid[0].size();
        // declare a days to rot vector of vectors
        vector<vector<int>> days(m,vector<int>(n,INT_MAX));
        int maxDays = INT_MIN;
        // now proceed to mark initially rotten oranges
        for(int i =0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==rotten){
                    days[i][j] = 0;
                }
                else if(grid[i][j]==none){
                    days[i][j] = INT_MIN;
                }
            }
        }
        
        // now do bfs on rotten oranges to mark new rotten oranges if any in vicinity
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
            if(days[i][j]>INT_MIN && days[i][j]<INT_MAX){
                    queue<pair<int,int>> q;
                    q.push({i,j});
                    while(!q.empty()){
                        auto cur = q.front();
                        q.pop();
                        vector<pair<int,int>> moves = {
                            {-1,0},
                            {1,0},
                            {0,1},
                            {0,-1}
                        };

                        for(auto move : moves){
                            auto I = cur.first+move.first, J = cur.second+move.second;

                            // check if adjacent index is valid
                            if(I>=0 && I<m && J>=0 && J<n){
                                if(days[I][J]!=INT_MIN){
                                    // check for only fresh oranges or previously rotten oranges (just in case a better value is possible)
                                    if(days[I][J]>days[cur.first][cur.second]+1){
                                        days[I][J] = days[cur.first][cur.second]+1;
                                        q.push({I,J});
                                    }
                                }
                            }

                        }
                    }
                }
            }
        }
        
        for(auto row:days){
            for(auto temp:row){
                maxDays = max(maxDays,temp);
            }
        }
        
        if(maxDays==INT_MIN) return 0;
        if(maxDays==INT_MAX) return -1;
        return maxDays;
        
    }
};