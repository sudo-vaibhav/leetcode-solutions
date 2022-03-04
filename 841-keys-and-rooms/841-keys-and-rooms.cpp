class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        set<int> visited;
        queue<int> q;
        q.push(0);
        visited.insert(0);
        
        while(!q.empty()){
            auto curRoom = q.front();
            q.pop();
            
            for(auto key: rooms[curRoom]){
                if(!visited.count(key)){
                    visited.insert(key);
                    q.push(key);
                }
            }
            
        }
        
        return visited.size()==n;
    }
};