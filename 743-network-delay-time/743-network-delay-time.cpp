class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int,int>>> adj(n+1);
        for(auto edge:times){
            adj[edge[0]].push_back({edge[1],edge[2]});
        }
        
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
        
        vector<int> minDist(n+1,INT_MAX);
        minDist[0] = INT_MIN;
        minDist[k] = 0;
        pq.push({k,0});
        
        while(!pq.empty()){
            auto cur = pq.top();
            pq.pop();
            
            for(auto edge: adj[cur.first]){
                if(minDist[cur.first]+edge.second<minDist[edge.first]){
                    minDist[edge.first] = cur.second + edge.second;
                    pq.push({edge.first,minDist[edge.first]});
                }
            }
        }
        
        auto dist = *max_element(minDist.begin(),minDist.end());
        return (dist == INT_MAX) ? -1 : dist;
    }
};