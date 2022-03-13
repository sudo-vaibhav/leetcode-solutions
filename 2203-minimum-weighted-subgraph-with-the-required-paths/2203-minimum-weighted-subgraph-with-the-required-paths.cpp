class Solution {
public:
    vector<long long> djikstra(vector<vector<pair<int,int>>>& adj,int src){
        priority_queue<pair<int,long long>,vector<pair<int,long long>>,greater<pair<int,long long>>> pq;
        vector<long long> res(adj.size(),LONG_LONG_MAX);
        res[src]=0;
        pq.push({src,0});
        while(!pq.empty()){
            auto cur = pq.top();pq.pop();
            if(cur.second!=res[cur.first]) continue;
            for(auto edge:adj[cur.first]){
                if(res[edge.first]>edge.second+cur.second){
                    res[edge.first]= edge.second+cur.second;
                    pq.push({edge.first,res[edge.first]});
                }
            }
        }
        
        return res;
    }
    long long minimumWeight(int n, vector<vector<int>>& edges, int src1, int src2, int dest) {
        vector<vector<pair<int,int>>> rev(n),adj(n);
        for(const auto &edge : edges){
            adj[edge[0]].push_back({edge[1],edge[2]});
            rev[edge[1]].push_back({edge[0],edge[2]});
        }
        
        auto fromSrc1 = djikstra(adj,src1),
        fromSrc2 = djikstra(adj,src2),
        fromDest = djikstra(rev,dest);
        
        long long ans = LONG_LONG_MAX;
        for(int i=0;i<n;i++){
            if(fromSrc1[i]==LONG_LONG_MAX||fromSrc2[i]==LONG_LONG_MAX||fromDest[i]==LONG_LONG_MAX){
                continue;
            }
            ans = min(ans, fromSrc1[i]+fromSrc2[i]+fromDest[i]);
        }
        
        return ans==LONG_LONG_MAX ? -1:ans;
    }
};