// Approach 1 using sets to store visited state, TLEs
// class Solution {
// public:
//     int shortestPathLength(vector<vector<int>>& graph) {
//         if(graph.size()<=1) return 0;
//         int n = graph.size();
        
//         queue<pair<int,set<int>>> q;
//         set<pair<int,set<int>>> seenState;
        
//         for(int i=0;i<n;i++) {
//             q.push({i,{i}});
//             seenState.insert({i,{i}});
//         };
        
//         int steps = 0;
        
//         while(!q.empty()){
//             auto qSize = q.size();
//             for(auto i=0;i<qSize;i++){
//                 auto curNode = q.front();
//                 q.pop();
//                 auto node = curNode.first;
                
//                 for(auto neighbor:graph[node]){
//                     auto newVisited = curNode.second;
//                     newVisited.insert(neighbor);
//                     if(newVisited.size()==n){
//                         return 1+steps;
//                     }
//                     if(!seenState.count({neighbor,newVisited})){
//                         seenState.insert({neighbor,newVisited});
//                         q.push({neighbor,newVisited});
//                     }
//                 }
//             }
//             steps++;
//         }
        
//         return -1;
//     }
// };


// Approach 2: Same approach as above but with bitmasks
class Solution {
public:
    int shortestPathLength(vector<vector<int>>& graph) {
        if(graph.size()<=1) return 0;
        int n = graph.size();
        
        queue<pair<int,int>> q;
        set<pair<int,int>> seenState;
        
        for(int i=0;i<n;i++) {
            q.push({i,1<<i});
            seenState.insert({i,1<<i});
        };
        
        int steps = 0;
        
        while(!q.empty()){
            auto qSize = q.size();
            for(auto i=0;i<qSize;i++){
                auto curNode = q.front();
                q.pop();
                auto node = curNode.first;
                
                for(auto neighbor:graph[node]){
                    auto newVisited = curNode.second;
                    // newVisited.insert(neighbor);
                    newVisited |= 1<<neighbor;
                    
                    if(newVisited==((1<<n)-1)){
                        return 1+steps;
                    }
                    if(!seenState.count({neighbor,newVisited})){
                        seenState.insert({neighbor,newVisited});
                        q.push({neighbor,newVisited});
                    }
                }
            }
            steps++;
        }
        
        return -1;
    }
};