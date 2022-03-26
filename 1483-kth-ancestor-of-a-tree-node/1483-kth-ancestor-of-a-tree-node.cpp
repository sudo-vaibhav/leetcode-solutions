class TreeAncestor {
public:
    vector<vector<int>> anc;
    int h;
    int n;
    TreeAncestor(int n, vector<int>& parent) {
        h = 20 ;//(int) ceil(log2(n))+1;
        this->n = n;
        anc = vector<vector<int>>(n,vector<int>(h,-1));
        // set 0th index ( which points to parent of that node)
        for (int i=0;i<n;i++){
            anc[i][0] = parent[i];
        }
        
        // set up jump pointers
        for(int j=1;j<h;j++){
            for(int i=0;i<n;i++){
                if(anc[i][j-1]==-1) {
                    anc[i][j] = -1;
                }
                else{
                    anc[i][j] = anc[ anc[i][j-1] ][j-1];
                }
            }
        }
        
        
    }
    
    int getKthAncestor(int node, int k) {
        auto cur = node;
        // if(cur<0 || cur>=n) return -1;
        for(int i=h-1;i>=0;--i){
            if(k&(1<<i)){
                
                cur = anc[cur][i];
                // k-=1<<i;
                if(cur==-1){
                    return -1;
                }
            }
        }
        return cur;
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */