class Solution {
public:
    int dfs(int source, vector<vector<int>>& adj ,vector<bool>& visited){
            int change = 0;
            visited[source]=true;
            for(auto dest:adj[source]){
                if(!visited[abs(dest)]){
                    change += dfs(abs(dest),adj,visited)+(dest>0);    
                }
            }
            
            return change;
    }
    int minReorder(int n, vector<vector<int>>& connections) {
        
        vector<vector<int>> adj(n,vector<int>());
        for (auto& c:connections){
            adj[c[0]].push_back(c[1]);
            adj[c[1]].push_back(-c[0]);
        }
        
        return dfs(0,adj,vector<bool>(n)={});
    }
};