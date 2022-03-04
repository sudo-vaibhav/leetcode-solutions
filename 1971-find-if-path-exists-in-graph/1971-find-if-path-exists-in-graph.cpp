class Solution {
public:
    map<int,int> mapping;
    void add(int x){
        if(!mapping.count(x)){
            mapping[x] = x;
        }
    }
    void doUnion(int x, int y){
        auto X = findParent(x);
        auto Y = findParent(y);
        
        if(X<Y) {
            mapping[X] = Y;
        }
        else{
            mapping[Y] = X;
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
        mapping = map<int,int>();
        for(auto edge:edges){
            add(edge[0]);
            add(edge[1]);
            doUnion(edge[0],edge[1]);
        }
        
        return findParent(source)==findParent(destination);
    }
};