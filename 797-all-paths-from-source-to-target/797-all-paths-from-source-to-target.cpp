class Solution {
public:
    void dfs(int node, int n, vector<vector<int>>& ans, set<int>& visited, vector<int>& path,
            vector<vector<int>>& graph
            ){
        visited.insert(node);
        path.push_back(node);
        if(node==n-1){
            ans.push_back(path);
        }
        else{
            for(auto neighbor : graph[node]){
                if(!visited.count(neighbor)){
                    dfs(neighbor,n,ans,visited,path,graph);
                }
            }
        }
        path.pop_back();
        visited.erase(node);
        
    }
    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> ans;
        set<int> visited;
        vector<int> path;
        int n = graph.size();
        dfs(0,n,ans,visited,path,graph);
        return ans;
    }
};