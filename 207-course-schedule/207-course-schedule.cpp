class Solution {
public:
    bool hasCycle(
        int node, vector<vector<int>>& adj, bool visited[],
        bool dfs[]
    ){
        dfs[node]=1;
        visited[node]=1;
        for(auto neighbor: adj[node]){
            if(!visited[neighbor]){
              if(hasCycle(neighbor,adj,visited,dfs)){
                  return true;
              }   
            }
            else{
               if(dfs[neighbor]) return true; 
            }
        }
        
        dfs[node]=0;
        return false;
    }
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        bool visited[numCourses], dfs[numCourses];
        memset(visited,false,numCourses);
        memset(dfs,false,numCourses);
        
        for(auto p:prerequisites){
            adj[p[1]].push_back(p[0]);
        }
        
        
        for(int i=0;i<numCourses;i++){
            if(!visited[i]){
                if(hasCycle(i,adj,visited,dfs)){
                    return false;
                }
            }
        }
        
        return true;
    }
};