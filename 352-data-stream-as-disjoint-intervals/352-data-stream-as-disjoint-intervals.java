/*
class UF{
    public:
    vector<int>parent;
    void unite(int u, int v){
        auto pu=find(u);
        auto pv=find(v);
        auto smaller = pu<pv ? pu:pv;
        auto larger = pu==smaller ? pv:pu;
        parent[smaller]=larger;
    }
    UF(){
        parent = vector<int>(pow(10,4)+1);
        for(int i=0;i<=pow(10,4);i++){
            parent[i]=i;
        }
    }
    int find(int v){
        if(parent[v]!=v){
            return v;
        }
        else{
            parent[v] = find(parent[v]);
            return parent[v];
        }
    }
};
class SummaryRanges {
public:
    set<int> nums;
    UF uf;
    SummaryRanges() {
        // nums = set<int>();
    }
    
    void addNum(int val) {
        nums.insert(val);
        if (nums.count(val-1)){
            uf.unite(val-1,val);
        }
        if (nums.count(val+1)){
            uf.unite(val,val+1);
        }
        
    }
    
    vector<vector<int>> getIntervals() {
        auto iter = nums.begin();
        vector<vector<int>> ans;
        while (iter!=nums.end()){
            auto end = nums.find(uf.find(*iter));
            ans.push_back({*iter,*end});
            iter = ++end;
        }
        return ans;
    }
};
*/
class UF{
    ArrayList<Integer>parent;
    
    public void unite(int u, int v){
        var pu=find(u);
        var pv=find(v);
        var smaller = pu<pv ? pu:pv;
        var larger = pu==smaller ? pv:pu;
        parent.set(smaller,larger);
    }
    public UF(){
        parent = new ArrayList<Integer>();
        for(int i=0;i<=Math.pow(10,4);i++){
            parent.add(i);
        }
    }
    public int find(int v){
        if(parent.get(v)==v){
            return v;
        }
        else{
            parent.set(v,find(parent.get(v)));
            return parent.get(v);
        }
    }
}
class SummaryRanges {
    TreeSet<Integer> nums;
    UF uf;
    public SummaryRanges() {
        nums = new TreeSet<>();
        uf = new UF();
    }
    
    public void addNum(int val) {
        nums.add(val);
        if (nums.contains(val-1)){
            uf.unite(val-1,val);
        }
        if (nums.contains(val+1)){
            uf.unite(val,val+1);
        }
    }
    
    public int[][] getIntervals() {
        var iter = nums.iterator();
        ArrayList<int[]> ans = new ArrayList<>();
        while (iter.hasNext()){
            var cur = iter.next(); 
            var endElem = uf.find(cur);
            var end = nums.tailSet(endElem).iterator();
            int[] temp = {cur,endElem}; 
            ans.add(temp);
            end.next();
            iter = end;
        }
        
        var ANS = new int[ans.size()][2];
        for(var i=0;i<ANS.length;i++){
            ANS[i] = ans.get(i);
        }
        return ANS;
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * int[][] param_2 = obj.getIntervals();
 */