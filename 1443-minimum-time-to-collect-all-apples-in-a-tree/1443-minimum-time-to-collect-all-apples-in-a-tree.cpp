class Solution {
public:
    // bfs like
    pair<bool, int> solve(
        const vector<vector<unsigned int>>& adj,
        const vector<bool>& hasApple,
        const unsigned int curNode,
        const unsigned int prev
    )
    {
        bool foundApple = false;
        unsigned int total =0;
        if(hasApple[curNode]){
            foundApple = true;
        }
        for(const auto& edge:adj[curNode]){
            if(prev!=edge){
                const auto temp = solve(adj,hasApple,edge,curNode);
                if(temp.first){
                    foundApple = true;
                    total += (2+ temp.second);
                }
            }
        }
        return {foundApple,total};
    }
    
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        vector<vector<unsigned int>> adj(n);
        for(auto const &edge:edges){
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        return solve(adj,hasApple,0,INT_MAX).second;
    }
};