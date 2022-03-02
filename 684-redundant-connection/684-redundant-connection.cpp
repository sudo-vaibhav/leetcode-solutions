class Solution {
public:
    
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
       
        map<int,set<int>> adj;
        
        auto canReach = []  (int node, int target,map<int,set<int>>& adj) mutable {
            // visited[i] = true;
            queue<int> q;
            q.push(node);
            set<int> visited;  
            while(!q.empty()){
                auto size = q.size();
                
                for(auto i=0;i<size;i++){
                    auto cur = q.front();
                    q.pop();
                    visited.insert(cur);
                    if(cur==target){
                        return true;
                    }
                    else{
                        for(auto neighbor: adj[cur]){
                            if(!visited.count(neighbor)){
                                q.push(neighbor); 
                            }
                        }
                    }
                }
                
            }
            
            return false;
        };
        
        for (auto edge:edges){
            // visited = set<int>();
            if(
               adj.count(edge[0])
               && adj.count(edge[1])
               && canReach(edge[0],edge[1],adj)
            ){
                return edge;
            }
            
            adj[edge[0]].insert(edge[1]);
            adj[edge[1]].insert(edge[0]);
        }
        
        return {-1,-1};
    }
};