class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        const char wall='+',empty='.';
        const int m=maze.size();
        const int n=maze[0].size();
        
        const vector<pair<int,int>> moves = {{-1,0},{1,0},{0,1},{0,-1}};
        queue<pair<int,int>> q;
        q.push({entrance[0],entrance[1]});
        maze[entrance[0]][entrance[1]]=wall;
        int steps = 0;
        while(!q.empty()){
            int queueSize = q.size();
            while(queueSize--){
                auto cur = q.front();q.pop();   
                if((cur.first==0 || cur.second==0||cur.first==m-1||cur.second==n-1)&& !(cur.first==entrance[0]&&cur.second==entrance[1])) return steps;
                for(const auto& move:moves){
                    const auto I = move.first+cur.first;
                    const auto J = move.second+cur.second;
                    if(I>=0 && I<m && J>=0 && J<n && maze[I][J]==empty){
                        maze[I][J] = wall;
                        q.push({I,J});
                    }
                }
            }
            steps++;
        }
        
        return -1;
    }
};