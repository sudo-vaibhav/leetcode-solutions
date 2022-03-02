// BFS approach
// class Solution {
// public:
    
//     vector<int> findRedundantConnection(vector<vector<int>>& edges) {
//         map<int,set<int>> adj;
//         auto canReach = [&](int node, int target) {
//             queue<int> q;
//             q.push(node);
//             set<int> visited;  
//             while(!q.empty()){
//                 auto size = q.size();
//                 while(size--){
//                     auto cur = q.front();
//                     q.pop();
//                     visited.insert(cur);
//                     if(cur==target) return true;
//                     else{
//                         for(auto neighbor: adj[cur]){
//                             if(!visited.count(neighbor)){
//                                 q.push(neighbor); 
//                             }
//                         }
//                     }
//                 }
                
//             }
//             return false;
//         };
        
//         for (auto edge:edges){
//             if(
//                adj.count(edge[0])
//                && adj.count(edge[1])
//                && canReach(edge[0],edge[1])
//             ){
//                 return edge;
//             }
//             adj[edge[0]].insert(edge[1]);
//             adj[edge[1]].insert(edge[0]);
//         }
        
//         return {-1,-1};
//     }
// };

class Solution {
public:
    
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        map<int,set<int>> adj;
        set<int> visited;  
        
        function<bool(int,int)> canReach = [&](int node, int target) {
            visited.insert(node);
            if(node==target) return true;
            else{
                for(auto neighbor: adj[node]){
                    if(!visited.count(neighbor)&&canReach(neighbor,target)) return true; 
                }
            }  
            return false;
        };
        
        for (auto edge:edges){
            visited = set<int>();
            if(
               adj.count(edge[0])
               && adj.count(edge[1])
               && canReach(edge[0],edge[1])
            ){
                return edge;
            }
            adj[edge[0]].insert(edge[1]);
            adj[edge[1]].insert(edge[0]);
        }
        
        return {-1,-1};
    }
};