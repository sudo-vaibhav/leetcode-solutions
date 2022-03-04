class Solution {
public:
    unordered_map<int,int> mapping;
    unordered_map<int,int> rank;
    void add(int x){
        if(!mapping.count(x)){
            mapping[x] = x;
            rank[x]=1;
        }
    }
    void doUnion(int x, int y){
        auto X = findParent(x);
        auto Y = findParent(y);
        if(X==Y) return;
        if(rank[X]<rank[Y]) {
            mapping[X] = Y;
            rank[Y] += rank[X];
        }
        else{
            mapping[Y] = X;
            rank[X] += rank[Y];
        }
    }
    int findParent(int x){
        if(x==mapping[x]){
            return x;
        }
        else{
            return mapping[x] = findParent(mapping[x]);
        }
    }
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        mapping = unordered_map<int,int>();
        rank = unordered_map<int,int>();
        for(auto edge:edges){
            add(edge[0]);
            add(edge[1]);
            doUnion(edge[0],edge[1]);
        }
        
        return findParent(source)==findParent(destination);
    }
};