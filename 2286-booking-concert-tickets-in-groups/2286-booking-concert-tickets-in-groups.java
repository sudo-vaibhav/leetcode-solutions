// note to self: 
// generally range updates are done when multiple leaf nodes are to be changed in a segment tree
// and this range update problem by itself is not very optimal
// this is where concept of lazy propogation helps and makes range update query logarithmic
// but in order to do lazy propogation, one needs to be able to efficiently recompute the current node using the lazy attribute
// in the push method, which sadly cannot be done for attributes maxi of this problem as we cant know what will be the new maxi value after lazy propogation 
// adjustment using the lazy attribute.

// so here we have to manually do point by point updates in case of a scatter operation, and to be able to do that with some degree of efficiency
// we keep an extra array tracking current available seats in each row apart from the segment tree array to formulate our commands properly to be given 
// to segment tree for point update

// also we can use a more easy to process update, instead of asking tree to reduce values of maxi and total itself by smartly recursing, we adopted
// a very similar point update query which just sets value in given row to provided value

class BookMyShow {

    class STNode{
        long maxi,total;    
        public STNode(long seatCount){
            maxi = seatCount;
            total = seatCount;
        }

        public STNode(long maxi,long total){
            this.maxi = maxi;
            this.total = total;
        }

        public STNode(){
            maxi = 0;
            total = 0;
        }
    }

    int n,m;
    STNode[] segTree;
    int[] availableSeats;
    
    
    public BookMyShow(int n, int m) {
        this.n = n;
        this.m = m;
        this.segTree = new STNode[4*n];
        this.buildSegTree(1,0,n-1);
        this.availableSeats = new int[n];
        Arrays.fill(this.availableSeats,m);
    }
    
    public STNode merge(STNode a, STNode b){
        return new STNode((long)Math.max(a.maxi,b.maxi),(long)(a.total+b.total));    
    }
    
    public void buildSegTree(int id,int l,int r){
            if(l>r) return;
            if(l==r){
                segTree[id] = new STNode(m);
            }
            else{
                var mid = l+(r-l)/2;
                buildSegTree(id*2,l,mid);
                buildSegTree(1+id*2,mid+1,r);
                segTree[id] = merge(segTree[id*2],segTree[2*id+1]);
            }
    }
    
    public int[] gatherQuery(int id, int l, int r, int seatsNeeded, int maxRow){
//         this first bit of if check is not something i have seen before, generally we are able to do early return 
//         in conditions like l<=lq<=rq<=r , but here max of segment is used to do early return (that too only in less than seatsNeeded case)
//         for maxi>=seatsNeeded case, you still need to query further \U0001f635
        if(segTree[id].maxi<seatsNeeded || maxRow<l){
            return new int[0];
        }
        
        if(l==r){
            if (this.segTree[id].total>=seatsNeeded){
                var res = new int[2];
                res[0] = l;
                res[1] = m-(int)this.segTree[id].total;
                return res;
            }
            else{
                return new int[0];
            }
        }
        int mid = l+(r-l)/2;
        var temp = gatherQuery(2*id,l,mid,seatsNeeded,maxRow);
        if (temp.length==0){
            return gatherQuery(2*id+1,mid+1,r,seatsNeeded,maxRow);
        }
        else{
            return temp;
        }
    }
    
    public long totalQuery(int id, int l, int r,int maxRow){
        if(maxRow<l){
            return 0;
        }
        if(r<=maxRow){
            return (long)segTree[id].total;
        }
        int mid = l+(r-l)/2;
        return totalQuery(2*id,l,mid,maxRow)+totalQuery(2*id+1,mid+1,r,maxRow);
    }
    
    public int[] gather(int k, int maxRow) {
        var coords = gatherQuery(1,0,n-1,k,maxRow);
        if (coords.length==2){
            update(1,0,n-1,coords[0],this.availableSeats[coords[0]]-k);
        }
        return coords;
    }
        
    public void update(int id, int l, int r, int targetRow, int newVal){
        if (targetRow<l || targetRow>r) return;
        if(l==r){
            if (l==targetRow){
                this.segTree[id].maxi = newVal;
                this.segTree[id].total = newVal;
                this.availableSeats[l]=newVal;
            }
        }
        else{
            int mid = l+(r-l)/2;
            update(2*id,l,mid,targetRow,newVal);
            update(2*id+1,mid+1,r,targetRow,newVal);
            this.segTree[id] = merge(this.segTree[2*id],this.segTree[2*id+1]);
        }
    }
    
    public boolean scatter(int k, int maxRow) {
        long totalAvailable = totalQuery(1,0,n-1,maxRow);
        if (totalAvailable<k){
            return false;
        }
        for(int row=0;row<=maxRow && k!=0;row++){
            var maxCanGet = Math.min(k,this.availableSeats[row]);
            if (maxCanGet>0){   
                update(1,0,n-1,row,this.availableSeats[row]-maxCanGet);
                k-=maxCanGet;
            }
        }        
        return true;
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow obj = new BookMyShow(n, m);
 * int[] param_1 = obj.gather(k,maxRow);
 * boolean param_2 = obj.scatter(k,maxRow);
 */