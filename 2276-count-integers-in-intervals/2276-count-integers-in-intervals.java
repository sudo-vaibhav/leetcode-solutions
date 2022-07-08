class Node{
    int l;
    int r;
    int val;
    Node lc,rc;
    public Node(int l,int r,int v){
        this.l = l;
        this.r = r;
        this.val = v;
        lc=null;
        rc=null;
    }
}
class CountIntervals {
    Node root;
    public CountIntervals() {
        root = new Node(1,1000000000,0);
    }
        
    void update(Node node, int ul,int ur){
        if (ul>node.r || ur<node.l) return;
        if (ul <= node.l && node.r<= ur){
            node.val = node.r-node.l+1;
            node.lc = null;
            node.rc = null;
            return;
        }
        int mid = node.l+(node.r-node.l)/2;
        if (node.lc==null){
            node.lc = new Node(node.l,mid,node.val > 0 ? mid - node.l + 1 : 0); 
        }
        if (node.rc==null){
            node.rc = new Node(mid+1,node.r,node.val > 0 ? node.r - mid : 0);
        }
        update(node.lc,ul,ur);
        update(node.rc,ul,ur);
        node.val = node.lc.val+node.rc.val;
    }
    
    public void add(int left, int right) {
        update(root,left,right);
    }
    
    public int count() {
        return root.val;
    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals obj = new CountIntervals();
 * obj.add(left,right);
 * int param_2 = obj.count();
 */